"""TypeSafe System One API クライアント。

公式 Python SDK (`typesafe-sdk`) もあるが、ここでは文書化されている HTTP
エンドポイントを直接叩いている。判定結果は審査記録として何年も残るので、
リクエスト/レスポンスの形を自分のコードの中で完全に把握できる状態にしておく
ことを優先した。SDK に寄せる場合は本ファイルだけ差し替えればよい。

  POST https://api.typesafe.ai/v1/systemone
  Authorization: Bearer $TYPESAFE_API_KEY
"""

from __future__ import annotations

import os
import random
import time
from typing import Any

import httpx

from .config import Rubric
from .models import Usage

DEFAULT_ENDPOINT = "https://api.typesafe.ai/v1/systemone"
DEFAULT_MODEL = "jev-latest"

# 応募資格 noul の質問 id 接頭辞。採点軸と衝突させないため。
ELIG_PREFIX = "elig_"
SCORE_PREFIX = "score_"
CATEGORY_KEY = "category"


class TypeSafeError(RuntimeError):
    pass


def build_questions(rubric: Rubric) -> dict[str, dict[str, Any]]:
    """ルーブリック1つから、1リクエストで投げる全質問を組み立てる。

    1件の応募につき API 呼び出しは1回。質問を分割すると件数分だけ state を
    読み直すことになり、コストも遅延も質問数に比例して増える。
    """
    questions: dict[str, dict[str, Any]] = {}

    for check in rubric.eligibility:
        questions[ELIG_PREFIX + check.id] = {
            "type": "noul",
            "instructions": check.instructions.strip(),
        }

    questions[CATEGORY_KEY] = {
        "type": "choice",
        "instructions": "Which award category does this work belong to?",
        "criteria": dict(rubric.categories),
    }

    for axis in rubric.scores:
        questions[SCORE_PREFIX + axis.id] = {
            "type": "score",
            "instructions": axis.instructions.strip(),
            "criteria": list(axis.criteria),
        }

    return questions


class TypeSafeClient:
    def __init__(
        self,
        api_key: str | None = None,
        *,
        endpoint: str = DEFAULT_ENDPOINT,
        model: str = DEFAULT_MODEL,
        timeout: float = 60.0,
        max_retries: int = 4,
    ) -> None:
        key = api_key or os.environ.get("TYPESAFE_API_KEY", "")
        if not key:
            raise TypeSafeError(
                "TYPESAFE_API_KEY が設定されていません。"
                " https://console.typesafe.ai/keys で取得して環境変数に入れてください。"
            )
        self.model = model
        self.endpoint = endpoint
        self.max_retries = max_retries
        self._client = httpx.Client(
            timeout=timeout,
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        )

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "TypeSafeClient":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    def ask(self, state: str, questions: dict[str, dict[str, Any]]) -> tuple[dict[str, Any], Usage]:
        """1件分を判定する。answers と usage を返す。"""
        payload = {"state": state, "model": self.model, "questions": questions}
        last_error: Exception | None = None

        for attempt in range(self.max_retries + 1):
            try:
                resp = self._client.post(self.endpoint, json=payload)
            except httpx.HTTPError as exc:
                last_error = exc
            else:
                if resp.status_code < 400:
                    body = resp.json()
                    usage = body.get("usage") or {}
                    return body.get("answers", {}), Usage(
                        input_tokens=int(usage.get("input_tokens", 0)),
                        output_tokens=int(usage.get("output_tokens", 0)),
                    )
                # 4xx はリトライしても同じ（429 を除く）。本文を添えて即座に上げる。
                if resp.status_code != 429 and resp.status_code < 500:
                    raise TypeSafeError(f"HTTP {resp.status_code}: {resp.text[:500]}")
                last_error = TypeSafeError(f"HTTP {resp.status_code}: {resp.text[:200]}")

            if attempt < self.max_retries:
                delay = (2**attempt) + random.uniform(0, 0.5)
                time.sleep(delay)

        raise TypeSafeError(f"{self.max_retries + 1} 回試行して失敗: {last_error}")


def parse_answers(answers: dict[str, Any], rubric: Rubric) -> dict[str, Any]:
    """API レスポンスをルーブリックの語彙に戻す。

    欠けている回答は黙って 0 で埋めず、missing に積んで呼び出し側に返す
    （0 埋めすると「自信を持って最低評価」と区別がつかなくなる）。
    """
    out: dict[str, Any] = {
        "eligibility": {},
        "scores": {},
        "score_confidence": {},
        "category": "",
        "category_confidence": 0.0,
        "category_probabilities": {},
        "missing": [],
    }

    for check in rubric.eligibility:
        a = answers.get(ELIG_PREFIX + check.id)
        if not isinstance(a, dict) or "noul" not in a:
            out["missing"].append(check.id)
            continue
        out["eligibility"][check.id] = float(a["noul"])

    cat = answers.get(CATEGORY_KEY)
    if isinstance(cat, dict) and "choice" in cat:
        out["category"] = str(cat["choice"])
        out["category_confidence"] = float(cat.get("confidence", 0.0))
        out["category_probabilities"] = {
            str(k): float(v) for k, v in (cat.get("probabilities") or {}).items()
        }
    else:
        out["missing"].append(CATEGORY_KEY)

    for axis in rubric.scores:
        a = answers.get(SCORE_PREFIX + axis.id)
        if not isinstance(a, dict) or "score" not in a:
            out["missing"].append(axis.id)
            continue
        out["scores"][axis.id] = float(a["score"])
        out["score_confidence"][axis.id] = float(a.get("confidence", 0.0))

    return out
