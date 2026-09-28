#!/usr/bin/env python3
"""Audit high lexical similarity between the fixed evaluation splits and training split."""
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

def main(root: Path, threshold: float) -> None:
    train = pd.read_csv(root / "BADD_train_bengali.csv")
    val = pd.read_csv(root / "BADD_validation_bengali.csv")
    test = pd.read_csv(root / "BADD_test_bengali.csv")
    all_text = pd.concat([train.comment, val.comment, test.comment], ignore_index=True).astype(str)
    vec = TfidfVectorizer(
        analyzer="char_wb", ngram_range=(3, 5), min_df=2,
        max_features=80000, sublinear_tf=True, dtype=np.float32
    )
    X = vec.fit_transform(all_text)
    ntr, nv = len(train), len(val)
    Xtr = X[:ntr]
    Xv = X[ntr:ntr+nv]
    Xt = X[ntr+nv:]
    nn = NearestNeighbors(n_neighbors=1, metric="cosine", algorithm="brute", n_jobs=-1)
    nn.fit(Xtr)
    for name, Xq in [("validation", Xv), ("test", Xt)]:
        dist, _ = nn.kneighbors(Xq, return_distance=True)
        sim = 1.0 - dist.ravel()
        count = int((sim >= threshold).sum())
        print(f"{name}: {count}/{len(sim)} ({100*count/len(sim):.2f}%) with nearest-train cosine >= {threshold:.2f}")
        print(f"  max={sim.max():.4f}; p95={np.quantile(sim, 0.95):.4f}; p99={np.quantile(sim, 0.99):.4f}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path("."))
    ap.add_argument("--threshold", type=float, default=0.95)
    args = ap.parse_args()
    main(args.root, args.threshold)
