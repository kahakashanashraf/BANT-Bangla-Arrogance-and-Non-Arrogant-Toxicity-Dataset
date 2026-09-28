# BANT Three-Class Release

**BANT** stands for **Bangla Arrogance and Non-Arrogant Toxicity Dataset**.

This folder contains the original three-class majority-vote task for BANT. The same three-class task is included in the **Mendeley Data Version 1** deposit (DOI: **10.17632/f8gxb8xcw6.1**).

The three labels are:

- `Arrogant`
- `Non-Arrogant-Toxic`
- `Non-Arrogant`

## Derivation

The three-class label is derived by row-wise majority voting across the three human annotation files. No AI/model prediction is used to determine the annotation label. The binary-compatible label is retained in every file:

- `Arrogant` → `Arrogant`
- `Non-Arrogant-Toxic` → `Non-arrogant`
- `Non-Arrogant` → `Non-arrogant`

## Counts

| Three-class label | Rows |
|---|---:|
| Arrogant | 6,126 |
| Non-Arrogant-Toxic | 9,183 |
| Non-Arrogant | 7,118 |
| **Total** | **22,427** |

## Fixed splits

The same row membership is retained across the binary and three-class tasks.

| Split | Rows |
|---|---:|
| Train | 17,941 |
| Validation | 2,243 |
| Test | 2,243 |

No re-splitting was performed.

## Files

Bengali, English, and aligned bilingual versions are provided for the full dataset and fixed train/validation/test splits.

Use `arrogance_label_3class` for the three-class task and `arrogance_label_binary` for the binary-compatible view.

## Citation

Please cite:

**Ashraf, Kahakashan (2026), “BANT: Bangla Arrogance and Non-Arrogant Toxicity Dataset”, Mendeley Data, V1, doi: 10.17632/f8gxb8xcw6.1.**

## License

CC BY 4.0.
