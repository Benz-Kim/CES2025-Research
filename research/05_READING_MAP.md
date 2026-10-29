# 05 — Reading map: mechanisms, deployment and demand

This map connects source contributions to decisions instead of treating references as a reading-count metric. See [the source register](../sources/REGISTER.md) for links and dates.

| Reading cluster | Sources | Question answered | Question left open |
| --- | --- | --- | --- |
| Final primitive standards | S01, S02, S16, S17 | Which cryptographic function is specified? | Is a particular product's system secure? |
| Algorithm design lineage | S03, S04, S05 | What construction and research artifacts underlie the primitive? | Does the deployment match the final standard? |
| Quantum attack resource model | S06 | How do assumptions shape a concrete attack-cost estimate? | When will the required hardware exist? |
| Banking experiments | S07, S09 | What integration issues arise in documented institutional tests? | How do they transfer to a different workload? |
| Migration framework | S08 | How can inventory and phased change structure a transition? | What will buyers pay a particular vendor? |
| Public analyst assessment | S10 | What product proposition did the analyst recognize? | Market share, independently verified security and representative pricing |
| Vendor positioning | S11, S12, S13 | What capability or category does the company present? | Independent proof and historical configuration |
| Open research software | S14, S15 | How are implementations, limitations and tests exposed? | Commercial product assurance |

## Synthesis

**Interpretation:** standards reduce ambiguity about primitive selection; they do not eliminate integration work. Institutional experiments move the question from “does a primitive exist?” to “can a specific system transition?” Commercial diligence then asks whether a provider makes that transition measurably easier.

The original deck's broad “future proofing” language should therefore be replaced with narrower questions about dependency discovery, upgrade authority and failure behavior. These questions can be investigated without pretending to know a quantum-computer arrival date.

## Priority evidence gaps

- Full-text, version-specific implementation analysis beyond the public source summaries used here.
- Independent PQC deployment results with explicit scope and negative findings.
- Buyer interviews and pricing evidence sufficient for a bottom-up demand estimate.
- Versioned Quranium architecture, security review and historical partnership evidence.
- Comparative operational cost for native platform upgrades versus independent orchestration.

The missing material is part of the research result. It identifies what would have to be learned before making a stronger recommendation.
