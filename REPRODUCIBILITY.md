# BANT reproducibility checks

The canonical dataset record is **BANT — Bangla Arrogance and Non-Arrogant Toxicity Dataset, Mendeley Data Version 1**, DOI **10.17632/f8gxb8xcw6.1**.

This repository provides both the binary task and the original three-class majority-vote task. Released dataset filenames use the canonical `BANT_*.csv` prefix.

## Release validation

From the repository root:

```bash
python reproducibility/validate_release.py --root .
```

The script checks row counts, label/source domains, category completeness, exact and normalized-text uniqueness, split disjointness and coverage, English/bilingual alignment, selected direct-identifier patterns, and the three-class companion counts.

## Cross-split near-duplicate audit

```bash
python reproducibility/near_duplicate_audit.py --root . --threshold 0.95
```

This is a sensitivity audit rather than a canonical split rewrite. Character TF-IDF nearest-neighbor screening finds 52/2,243 validation rows (2.3%) and 66/2,243 test rows (2.9%) with cosine similarity of at least 0.95 to a training comment. These are mostly short or word-order-variant social-media expressions. The fixed split membership is retained for version compatibility; researchers can report a stricter sensitivity analysis after excluding flagged evaluation rows.

## Sanity-check baseline

Install the pinned environment and run:

```bash
python -m pip install -r reproducibility/requirements.txt
python reproducibility/baseline_tfidf.py --root .
```

The benchmark uses character TF-IDF (`char_wb`, 3–5 grams, `min_df=2`, up to 120,000 features) followed by class-weighted logistic regression with `random_state=42`. It is intended only as a reproducibility/usability check, not as a state-of-the-art benchmark.

On the full binary test set, macro-F1 is 0.8846. Restricting evaluation to rows whose maximum character-TF-IDF similarity to training is below 0.95 yields macro-F1 0.8806.

## Collection-code note

A preserved historical Facebook collection notebook was used to recover the Selenium version and collection mechanics, but it is not published because the notebook contains historical authentication material. No credentials are required to use or validate the released dataset.

## Citation

Ashraf, Kahakashan (2026), “BANT: Bangla Arrogance and Non-Arrogant Toxicity Dataset”, Mendeley Data, V1, doi: 10.17632/f8gxb8xcw6.1.
