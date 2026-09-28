# BANT Human Annotation Guideline

**BANT** stands for **Bangla Arrogance and Non-Arrogant Toxicity Dataset**. The archived Mendeley Data Version 7 record and legacy `BADD_*.csv` filenames retain the earlier BADD name for compatibility.

## Purpose
Annotators judge each Bangla social-media comment from its overall meaning, tone, context, and pragmatic intent. Annotation decisions are based only on human judgment.

## Human annotation labels
- **Arrogant** — expresses superiority, self-importance, entitlement, condescension, dominance, or a dismissive sense that the speaker or group is better, more knowledgeable, or more deserving than others.
- **Non-Arrogant-Toxic** — contains insult, hostility, abuse, ridicule, or other toxic language but does not clearly express arrogance or superiority.
- **Non-Arrogant** — does not express arrogance. Ordinary opinion, disagreement, criticism, humour, factual statements, or neutral comments belong here when superiority is absent.

## Arrogance categories
For comments labelled Arrogant, select the most appropriate category:
- Superiority & Self-Importance
- Knowledge & Moral Superiority
- Contempt & Condescension
- Dominance & Entitlement
- Mixed / Other Arrogance

## Decision rules
- Read the entire comment before assigning a label; do not decide from a single keyword.
- Distinguish toxicity from arrogance: an insult alone is not automatically Arrogant.
- Strong criticism or disagreement is not arrogance unless superiority, entitlement, contempt, dominance, or condescension is expressed.
- Consider sarcasm, irony, slang, code-mixing, emojis, and culturally specific expressions in context.
- Ignore personal agreement or disagreement and judge only communicative meaning.
- Do not use model predictions or automated confidence signals to determine labels.

## Annotation protocol
The dataset was reviewed by exactly **three human annotators**. Each annotator received a separate copy of the annotation material and submitted a label and, for Arrogant comments, one of the five fine-grained categories.

Before the main annotation activity, the annotators received an online briefing from **Md. Golam Mostafa** on the label definitions, category boundaries, and practical decision rules. During annotation, an annotator could contact him when a guideline or ambiguous example was unclear. These consultations were for clarification of the annotation rules rather than post-hoc group adjudication of submitted disagreements.

The annotators did not use a confidence field in the released annotation files. No AI system, model prediction, or model-derived signal was used as an annotator or as a source of human consensus.

Because the material included abusive and psychologically unpleasant language, annotators were advised to take a break approximately every 30 minutes to reduce prolonged exposure to disturbing content.

## Consensus
The archived annotation files preserve the three submitted human labels. Final release labels are derived computationally by majority vote.

For the Mendeley Version 7 binary task:
- `Arrogant` remains `Arrogant`.
- `Non-Arrogant-Toxic` and `Non-Arrogant` map to `Non-arrogant`.

The GitHub-only `three_class_release/` companion preserves the original three-class majority-vote labels and is the recommended resource for researchers who want to model the full BANT label distinction.

## Acknowledgment
We gratefully acknowledge **Md. Golam Mostafa, Assistant Professor, Department of Bengali, Cox's Bazar Government College, Cox's Bazar**, for linguistic guidance, the pre-annotation briefing, clarification of ambiguous cases, and review of the AI-originated Bangla examples.
