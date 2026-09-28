# BANT reproducibility checks

**BANT** is the current project name: **Bangla Arrogance and Non-Arrogant Toxicity Dataset**. The Mendeley Data Version 7 files and legacy `BADD_*.csv` filenames retain the earlier BADD name for archival and code compatibility.

The Mendeley Data Version 7 files remain the canonical binary release. The GitHub `three_class_release/` directory is an optional companion that preserves the original three-class majority-vote task without altering V7.

## Release validation

From the repository root:

```bash
python reproducibility/validate_release.py --root .
```

The script checks row counts, label/source domains, category completeness, exact and normalized-text uniqueness, split disjointness and coverage, English/bilingual alignment, selected direct-identifier patterns, and (when present) the three-class companion counts.

## Cross-split near-duplicate audit

```bash
python reproducibility/near_duplicate_audit.py --root . --threshold 0.95
```

This is a sensitivity audit rather than a canonical split rewrite. Character TF-IDF nearest-neighbor screening finds 52/2,243 validation rows (2.3%) and 66/2,243 test rows (2.9%) with cosine similarity of at least 0.95 to a training comment. These are mostly short or word-order-variant social-media expressions. The fixed Version 7 split membership is retained for version compatibility; researchers can report a stricter sensitivity analysis after excluding flagged evaluation rows.

## Sanity-check baseline

Install the pinned environment and run:

```bash
python -m pip install -r reproducibility/requirements.txt
python reproducibility/baseline_tfidf.py --root .
```

The benchmark uses character TF-IDF (`char_wb`, 3–5 grams, `min_df=2`, up to 120,000 features) followed by class-weighted logistic regression with `random_state=42`. It is intended only as a reproducibility/usability check, not as a state-of-the-art benchmark.

On the full binary test set, macro-F1 is 0.8846. Restricting evaluation to rows whose maximum character-TF-IDF similarity to training is below 0.95 yields macro-F1 0.8806, indicating that the lightweight sanity-check conclusion is not driven by the high-similarity subset.

## Collection-code note

A preserved historical Facebook collection notebook was used to recover the Selenium version and collection mechanics, but it is not published because the notebook contains historical authentication material. No credentials are required to use or validate the released dataset.
