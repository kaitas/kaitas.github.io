from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from award_triage.config import load_fieldmap, load_rubric  # noqa: E402
from award_triage.ingest import detect_language, load_entries  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def test_detect_language():
    assert detect_language("これはテストです") == "ja"
    assert detect_language("기억의 정원") == "ko"
    assert detect_language("城市呼吸") == "zh"
    assert detect_language("Prompt Garden") == "latin"
    assert detect_language("   ") == ""
    # 漢字とかなが混ざれば日本語
    assert detect_language("残響の街") == "ja"


def test_load_sample_entries():
    entries = load_entries(ROOT / "samples" / "entries.sample.csv", load_fieldmap())
    assert len(entries) == 8
    by_id = {e.entry_id: e for e in entries}
    assert by_id["E-001"].source_language == "ja"
    assert by_id["E-003"].fields["title"] == "기억의 정원"
    # 公開日が空の応募には警告がつく
    assert any("published_at" in w or "description" in w for w in by_id["E-006"].ingest_warnings) \
        or by_id["E-006"].fields["published_at"] == ""


def test_judge_text_excludes_personal_fields():
    """一次審査は氏名を伏せる。creator も credits もモデルに渡らない。"""
    fm = load_fieldmap()
    rubric = load_rubric()
    entries = load_entries(ROOT / "samples" / "entries.sample.csv", fm)
    text = entries[0].text_for(rubric.canonical_language, fm.judge_fields)
    assert "山田花子" not in text   # creator
    assert "佐藤一郎" not in text   # credits に入っている共同制作者
    assert "残響の街" in text
