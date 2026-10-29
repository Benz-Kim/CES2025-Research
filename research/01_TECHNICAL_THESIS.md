# 01 — The migration problem behind the algorithm

## Thesis

**Project interpretation:** PQC becomes useful when the surrounding system can adopt it without losing authentication, availability or operational control. Algorithm selection is necessary; migration architecture is the harder commercial test.

## What the primitives actually change

| Primitive | Function | Candidate lineage | Engineering question |
| --- | --- | --- | --- |
| ML-KEM, FIPS 203 | Establish a shared secret | CRYSTALS-Kyber | How is the peer authenticated, and how is the secret used? |
| ML-DSA, FIPS 204 | Sign and verify messages | CRYSTALS-Dilithium | What changes in certificates, signing services and verification paths? |
| SLH-DSA, FIPS 205 | Stateless hash-based signatures | SPHINCS+ | Where do size and runtime constraints permit its use? |

Sources: S01, S02, S16, S17 in [the register](../sources/REGISTER.md). These are different functions, not three interchangeable encryption products. Standards establish specified constructions and assumptions, not absolute immunity from every future attack.

A KEM does not by itself authenticate its peer or supply a complete application protocol. A product using a standardized primitive may still have failures in key storage, random-number generation, downgrade handling or software updates. The review must identify the boundary of protection.

## From research mechanism to system claim

**Reading note — Kyber (S03):** the original paper introduces a module-lattice KEM. Its contribution is a cryptographic construction under explicit assumptions. The useful question for product diligence is whether the deployed implementation matches the intended final standard and parameter set. The historical candidate name is not enough.

**Reading note — Dilithium (S04, S05):** the paper and supporting specification concern signatures, with reference materials and test vectors available. This moves the review toward reproducibility: identify version, implementation and tests. It does not establish that a particular vendor's complete signing pipeline is correct.

**Reading note — Gidney and Ekerå (S06):** the paper estimates resources for an RSA attack under a stated quantum-computing model. Its title's numerical estimate is conditional. It cannot establish a calendar date at which RSA becomes breakable in practice. Migration planning should therefore test uncertainty rather than choose a single “Q-day.”

## PQC and QKD: use-case comparison

PQC uses algorithms on classical computing systems; quantum key distribution uses quantum communication mechanisms and associated infrastructure. They address overlapping security objectives through different deployment assumptions (D01, S08). Neither label establishes protection for an entire organization.

**Project interpretation:** compare them through the actual communication path: endpoint ownership, distance, hardware availability, authentication and operational burden. A generalized “software versus hardware” slide is an introduction, not a procurement conclusion.

## Conditional urgency

Define a planning screen, not a probability model:

`exposure window = required confidentiality lifetime + migration lead time`

If the screen's window extends beyond an organization's assumed threat horizon, waiting may expose long-lived information to collection today and later decryption. The horizon remains an assumption. Record several horizons and show whether the migration decision changes.

This confidentiality argument differs from the future forgery risk to signatures. A signature system also needs a plan for long-lived verification, timestamping and trust anchors; encrypting network traffic does not solve all of those problems.

## What would weaken the thesis?

- Major platforms may provide sufficient PQC support at low incremental cost, reducing demand for a separate orchestration layer.
- Some systems may have short information lifetimes and straightforward replacement cycles.
- An added proxy or service can introduce operational and trust dependencies that exceed its migration benefit.

These are competing interpretations to investigate, not established market outcomes.

## Decision

Proceed from algorithm names to an inventory of protected paths and measurable failure conditions. The next documents apply that discipline to [commercial demand](02_MARKET_STRUCTURE.md) and [the two company cases](03_COMPANY_DILIGENCE.md).
