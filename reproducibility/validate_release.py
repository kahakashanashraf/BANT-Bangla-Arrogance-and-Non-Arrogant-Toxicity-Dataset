#!/usr/bin/env python3
"""Validate the BANT V1-compatible repository release and three-class companion."""
from __future__ import annotations
import argparse, re, unicodedata
from pathlib import Path
import pandas as pd

def canonical_text(text: str) -> str:
    s = unicodedata.normalize("NFKC", str(text))
    for ch in ["​", "‌", "‍", "﻿"]:
        s = s.replace(ch, "")
    return re.sub(r"\s+", " ", s.lower()).strip()

def main(root: Path) -> None:
    full = pd.read_csv(root / "BANT_final_dataset_bengali.csv")
    train = pd.read_csv(root / "BANT_train_bengali.csv")
    val = pd.read_csv(root / "BANT_validation_bengali.csv")
    test = pd.read_csv(root / "BANT_test_bengali.csv")
    eng = pd.read_csv(root / "BANT_final_dataset_english.csv")
    bilingual = pd.read_csv(root / "BANT_final_dataset_bilingual.csv")

    assert len(full) == 22427
    assert full["comment"].isna().sum() == 0
    assert set(full["source"]) == {"YouTube", "Facebook", "News portal", "AI"}
    assert full["arrogance_label"].value_counts().to_dict() == {"Non-arrogant": 16301, "Arrogant": 6126}
    assert full.loc[full.arrogance_label.eq("Arrogant"), "category"].notna().all()
    assert full.loc[full.arrogance_label.eq("Non-arrogant"), "category"].isna().all()
    assert full["comment"].duplicated().sum() == 0
    assert full["comment"].map(canonical_text).duplicated().sum() == 0

    split_sets = [set(x.comment.map(canonical_text)) for x in (train, val, test)]
    assert [len(train), len(val), len(test)] == [17941, 2243, 2243]
    assert not (split_sets[0] & split_sets[1])
    assert not (split_sets[0] & split_sets[2])
    assert not (split_sets[1] & split_sets[2])
    assert set.union(*split_sets) == set(full.comment.map(canonical_text))

    assert len(eng) == len(full) and eng.comment.astype(str).str.strip().ne("").all()
    assert len(bilingual) == len(full)
    assert bilingual.comment_bn.astype(str).equals(full.comment.astype(str))
    assert bilingual.source.equals(full.source)
    assert bilingual.arrogance_label.equals(full.arrogance_label)

    pii_patterns = {
        "url": r"https?://\S+|www\.\S+",
        "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
        "handle": r"(?<!\w)@[A-Za-z0-9_\.]{2,}",
        "bd_phone": r"(?<!\d)(?:\+?88)?01[3-9]\d{8}(?!\d)",
    }
    for name, pattern in pii_patterns.items():
        assert full.comment.astype(str).str.contains(pattern, regex=True).sum() == 0, name

    three_dir = root / "three_class_release"
    if three_dir.exists():
        three = pd.read_csv(three_dir / "BANT_final_dataset_bengali_3class.csv")
        assert len(three) == len(full)
        assert three.comment.equals(full.comment)
        assert three.source.equals(full.source)
        assert three.arrogance_label_binary.equals(full.arrogance_label)
        assert three.arrogance_label_3class.value_counts().to_dict() == {
            "Non-Arrogant-Toxic": 9183, "Non-Arrogant": 7118, "Arrogant": 6126,
        }

    print("BANT V1 repository validation passed.")
    print("Rows: 22,427 | splits: 17,941 / 2,243 / 2,243")
    print("Three-class labels: 6,126 Arrogant / 9,183 Non-Arrogant-Toxic / 7,118 Non-Arrogant")
    print("Binary labels: 6,126 Arrogant / 16,301 Non-arrogant")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path("."))
    main(ap.parse_args().root)
