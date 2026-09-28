# BANT — Bangla Arrogance and Non-Arrogant Toxicity Dataset

**BANT** is a human-annotated Bangla social-media dataset designed for **arrogance detection, non-arrogant toxicity analysis, fine-grained arrogance classification, and multilingual NLP research**. The canonical release contains **22,427 comments** and is deposited as **Mendeley Data Version 1**.

> **Canonical citation:** Ashraf, Kahakashan (2026), “BANT: Bangla Arrogance and Non-Arrogant Toxicity Dataset”, Mendeley Data, V1, doi: **10.17632/f8gxb8xcw6.1**.

Three human annotators reviewed separate copies of the annotation material. No AI/model prediction is used as an annotator or in the human label-consensus procedure.

> **Important:** the value `AI` in the `source` column denotes a data-provenance/source category. It does **not** mean an AI system annotated those rows.

## Current release

- **Dataset:** BANT — Bangla Arrogance and Non-Arrogant Toxicity Dataset
- **Mendeley Data version:** V1
- **DOI:** 10.17632/f8gxb8xcw6.1
- Canonical Bengali dataset: **22,427 rows**
- Train: **17,941**
- Validation: **2,243**
- Test: **2,243**
- Binary label space: `Arrogant` / `Non-arrogant`
- Three-class label space: `Arrogant`, `Non-Arrogant-Toxic`, and `Non-Arrogant`
- Arrogant rows additionally include one of five fine-grained categories.

## Why BANT?

The name emphasizes the distinction that motivates the annotation design: **toxic language is not automatically arrogant**. The dataset therefore supports both a binary arrogance task and a three-class task that explicitly separates `Non-Arrogant-Toxic` from ordinary `Non-Arrogant` content.

## Main files

This repository retains the existing `BADD_*.csv` filenames for backward code compatibility. The current dataset identity and citation are **BANT V1**.

- `BADD_final_dataset_bengali.csv` — Bengali binary release
- `BADD_final_dataset_english.csv` — machine-translated English companion
- `BADD_final_dataset_bilingual.csv` — aligned Bengali + English text
- `BADD_train_bengali.csv`, `BADD_validation_bengali.csv`, `BADD_test_bengali.csv`
- Matching English split files
- `three_class_release/` — three-class Bengali, English, and bilingual files with matching fixed splits
- `ANNOTATION_GUIDELINE.md`
- `DATA_DICTIONARY.csv`
- `TRANSLATION_METADATA.json`
- `TRANSLATION_QA_SUMMARY.md`
- `SHA256SUMS.txt`

## Three-class release

The `three_class_release/` folder preserves the original majority-vote three-class task. This task is also included in the BANT Mendeley Data V1 deposit.

- Arrogant: **6,126**
- Non-Arrogant-Toxic: **9,183**
- Non-Arrogant: **7,118**

The three-class release is available in Bengali, English, and bilingual forms with matching train/validation/test splits.

## Binary label counts

- Non-arrogant: **16,301**
- Arrogant: **6,126**

The binary view is derived as follows:

- `Arrogant` → `Arrogant`
- `Non-Arrogant-Toxic` → `Non-arrogant`
- `Non-Arrogant` → `Non-arrogant`

## Source distribution

- YouTube: **10,081**
- Facebook: **5,881**
- News portal: **5,547**
- AI: **918** (source/provenance category only)

## Annotation

Exactly three human annotators reviewed separate copies of the annotation material. Before annotation, they received a common briefing on the label definitions and decision rules. Annotators could seek clarification from Md. Golam Mostafa when a rule or ambiguous example was unclear; these consultations were for guideline clarification, not post-hoc group adjudication.

The archived annotation exports contain **22,421 unanimous three-class rows** and **6 majority-vote disagreements**. No AI/model prediction was used as an annotator or consensus signal.

## English companion translation

The English companion was generated from the finalized Bengali release with `facebook/nllb-200-distilled-600M` (`ben_Beng` → `eng_Latn`) using deterministic beam search (`num_beams=2`, `do_sample=False`). Translation changes only comment text; source, labels, and categories are copied unchanged.

Automatic QA currently flags **197 rows** for manual inspection. These flags are screening signals and are **not** confirmed translation errors.

## Reproducibility

See `REPRODUCIBILITY.md` and `reproducibility/` for release-integrity checks, cross-split similarity auditing, and a lightweight TF-IDF/logistic-regression sanity benchmark.

## Acknowledgment

We gratefully acknowledge **Md. Golam Mostafa, Assistant Professor, Department of Bengali, Cox's Bazar Government College, Cox's Bazar**, for linguistic guidance, the pre-annotation briefing, clarification of ambiguous cases, and review of the AI-originated Bangla examples.

## License and citation

BANT Mendeley Data Version 1 is released under **CC BY 4.0**.

Please cite:

**Ashraf, Kahakashan (2026), “BANT: Bangla Arrogance and Non-Arrogant Toxicity Dataset”, Mendeley Data, V1, doi: 10.17632/f8gxb8xcw6.1.**
