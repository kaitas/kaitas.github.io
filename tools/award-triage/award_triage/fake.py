"""API キー無しでパイプライン全体を動かすためのダミー判定器。

用途は2つだけ:
  * 審査委員に「画面と帳票がどう出るか」を見せる（鍵の発行を待たずに議論を始める）
  * CI / 手元でのリグレッション確認

判定の中身は本文の長さや語の有無から作った決め打ちで、審査としての意味は
一切ない。run --fake で使ったときは出力にその旨が明記される。
"""

from __future__ import annotations

import hashlib
import re
from typing import Any

from .config import Rubric
from .models import Usage
from .typesafe import CATEGORY_KEY, ELIG_PREFIX, SCORE_PREFIX


def _jitter(state: str, salt: str) -> float:
    """同じ入力には必ず同じ値を返す 0.0-1.0 の疑似乱数。"""
    h = hashlib.sha256((salt + state).encode("utf-8")).digest()
    return int.from_bytes(h[:4], "big") / 0xFFFFFFFF


class FakeTypeSafeClient:
    model = "fake"

    def close(self) -> None:  # pragma: no cover - インターフェース合わせ
        pass

    def __enter__(self) -> "FakeTypeSafeClient":
        return self

    def __exit__(self, *exc: object) -> None:
        pass

    def __init__(self, rubric: Rubric) -> None:
        self.rubric = rubric

    def ask(self, state: str, questions: dict[str, dict[str, Any]]) -> tuple[dict, Usage]:
        answers: dict[str, Any] = {}
        length = len(state)
        has_date = bool(re.search(r"published_at: \S", state))
        gated = bool(re.search(r"(members\.|/private/|patreon|login|ログイン)", state, re.I))
        thin = length < 220

        for key, q in questions.items():
            if q["type"] == "noul":
                cid = key[len(ELIG_PREFIX):]
                base = 0.92 + 0.07 * _jitter(state, key)
                if cid == "public_window" and not has_date:
                    base = 0.05
                if cid == "publicly_viewable" and gated:
                    base = 0.04
                if cid in ("genuine_entry", "genai_disclosed") and thin:
                    base = 0.08
                answers[key] = {"type": "noul", "noul": round(base, 3)}

            elif q["type"] == "choice":
                criteria = list(q["criteria"])
                # 申告カテゴリが本文にあればそれを、無ければ決め打ち
                declared = re.search(r"category: (\S+)", state)
                pick = declared.group(1) if declared and declared.group(1) in criteria else criteria[0]
                conf = 0.45 + 0.5 * _jitter(state, key)
                probs = {c: round((1 - conf) / max(1, len(criteria) - 1), 3) for c in criteria}
                probs[pick] = round(conf, 3)
                answers[key] = {
                    "type": "choice", "choice": pick,
                    "probabilities": probs, "confidence": round(conf, 3),
                }

            elif q["type"] == "score":
                top = len(q["criteria"]) - 1
                # 本文が長く具体的なほど高めに出る、という程度の相関
                base = min(top, (length / 320.0) * top * 0.75)
                val = max(0.0, min(float(top), base + (_jitter(state, key) - 0.5)))
                answers[key] = {
                    "type": "score", "score": round(val, 3),
                    "legend": {str(i): c for i, c in enumerate(q["criteria"])},
                    "confidence": round(0.5 + 0.45 * _jitter(state, key + "c"), 3),
                }

        # トークン数は概算（コスト表示の桁感を合わせるためだけ）
        return answers, Usage(input_tokens=length // 4, output_tokens=len(questions) * 6)


def is_fake(client: object) -> bool:
    return isinstance(client, FakeTypeSafeClient)
