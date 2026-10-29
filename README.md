# CES 2025 Research
### From quantum-security claims to a migration case

An evidence-led research project examining post-quantum cryptography, the commercial work of migration, and the difference between a promising technology claim and a decision a buyer can defend.

**Core thesis:** the important question is not simply whether a post-quantum algorithm exists. It is whether an organization can find its cryptographic dependencies, change them safely, and verify the resulting protection. The repository develops that thesis through standards, original research, institutional experiments, public analyst material and two company cases.

**Research status:** source-based analysis expanded on 2026-10-29. The CES 2025 label identifies the event context, not the date of every document or a claim of attendance. No vendor performance benchmark, customer interview or original cryptographic implementation is claimed.

## Findings at a glance

| Finding | Why it matters | Read the argument |
| --- | --- | --- |
| Key establishment and signatures are different migration tasks | A generic “PQC-enabled” label conceals important boundaries | [Technical thesis](research/01_TECHNICAL_THESIS.md) |
| Integration and assurance may matter as much as algorithm selection | Standards do not replace inventory, interoperability and rollback work | [Market structure](research/02_MARKET_STRUCTURE.md) |
| QuSecure and Quranium require different evidence questions | Orchestration positioning and a blockchain category claim should not be scored as equivalent artifacts | [Company diligence](research/03_COMPANY_DILIGENCE.md) |
| A credible product claim must survive failure tests | Connection success alone does not establish security or operational value | [Validation design](research/04_VALIDATION_DESIGN.md) |
| HoloDisplay is a useful contrast case | An innovation award establishes recognition, not every technical or commercial claim in a presentation | [Display comparison](research/06_DISPLAY_COMPARISON.md) |

These are project interpretations with explicit limitations, rather than measured vendor rankings or market forecasts.

## Read as a research brief

1. [The mechanism and threat assumptions](research/01_TECHNICAL_THESIS.md)
2. [Where commercial value may accrue](research/02_MARKET_STRUCTURE.md)
3. [What the company evidence does and does not support](research/03_COMPANY_DILIGENCE.md)
4. [How the thesis could be tested or rejected](research/04_VALIDATION_DESIGN.md)
5. [How the readings connect](research/05_READING_MAP.md)

For provenance, start with the [source register](sources/REGISTER.md), [original-material review](sources/DECK_REVIEW.md) and [research protocol](research/RESEARCH_PROTOCOL.md). The corpus includes NIST standards, Kyber and Dilithium design papers, a quantum attack-resource paper, BIS implementation research and a public Frost & Sullivan assessment. Full paid analyst datasets and representative customer economics were not available; no unsupported TAM or CAGR is presented.

## Project materials and contribution

The supplied materials include a PQC presentation discussing QuSecure and Quranium, plus team preparation slides and a script covering quantum computing and Samsung HoloDisplay. Original links and provider dates are recorded in the source register. Team authorship is preserved as team provenance; this repository does not infer unverified individual roles or event participation.

The repository adds an auditable argument: claim corrections, bounded company assessments, commercial alternatives, counterarguments and proposed measurements. Later institutional work is labeled retrospective; current vendor pages are not treated as historical product specifications.

## What would change the conclusion?

Independent deployments with defined scope, reproducible performance results, platform-native alternatives, customer budget evidence, or a versioned security analysis could strengthen or reverse the thesis. [The reading map](research/05_READING_MAP.md) identifies the most consequential gaps.

## Maintain and verify

Run `python3 scripts/validate_research.py` from the repository root to check local Markdown links and source-ID references. This is a structural check, not source verification or a security assessment.

[Contributing](CONTRIBUTING.md) defines evidence and update requirements. [Format rationale](research/FORMAT_RATIONALE.md) explains the open-research conventions used. Linked publications remain with their original owners; no third-party reports are redistributed.
