# Translation QA summary

- Current release rows: **22,427**
- Automatic QA flagged rows: **197**
- Reproducible QA sample: **500 rows**
- Translation model: `facebook/nllb-200-distilled-600M`
- Source/target: `ben_Beng` → `eng_Latn`
- Deterministic generation: `num_beams=2`, `do_sample=False`

Automatic QA flags include empty output checks, Bengali-script leakage in English output, identical source/target strings, and extreme character-length ratios. A flag is a **screening signal only** and must not be reported as a confirmed translation error without human review.

The Bengali dataset is the canonical language version. The English dataset is a machine-translated companion.
