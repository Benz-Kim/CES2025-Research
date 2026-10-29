# 04 — A validation design that can falsify the thesis

Status: proposed protocol. No cryptographic performance experiment has been executed in this repository.

## Hypothesis

An added migration layer is valuable only if it improves coverage or operational change capability while meeting the application's predeclared reliability and security requirements.

## Controlled comparison

| Item | Design requirement |
| --- | --- |
| Baseline | Existing classical configuration, documented before changes |
| Candidate | Exact PQC or hybrid configuration with versioned library, protocol and parameters |
| Environment | Same hardware, operating system, network topology and background load |
| Workloads | Connection setup, steady-state traffic, reconnection, certificate renewal and peak load |
| Repetition | Predeclare warm-up, sample count and independent run conditions |
| Failures | Unsupported peer, malformed input, key rotation, service outage and rollback |
| Evidence | Raw observations, logs, configuration hashes and exact commands |

## Measurements

Report connection-success rate; p50, p95 and p99 setup latency; throughput; CPU and memory; handshake bytes; error types; and rollback duration. Keep complete distributions and failed runs. Choose acceptance limits from application requirements before observing candidate results; no universal threshold is supplied.

Do not subtract medians and call the result a statistically established effect. Record paired runs where practical, uncertainty intervals and any confounding changes. A favorable average can conceal a tail-latency or compatibility failure.

## Security boundary

State what is protected between which endpoints. Inventory certificate paths, key stores, update signatures and logs that may remain outside that boundary. Verify key custody and privileged management access. A successful connection is not a security proof.

For hybrid designs, identify the exact combiner and negotiation rules. Do not assume that concatenating algorithms automatically preserves both security properties. Review downgrade behavior and authentication separately.

## Reproducibility sequence

1. Pin the implementation revision and record dependencies.
2. Commit configuration and a machine-readable run manifest without secrets.
3. Capture baseline and candidate observations using the same instrumentation.
4. Retain failed cases and explain exclusions before calculating summaries.
5. Publish a result note distinguishing observed behavior from inferred security.
6. Repeat on an independently configured environment before generalizing.

S14 and S15 offer useful research-software conventions: explicit scope, implementation visibility and test surfaces. They are starting references, not evidence that this proposed design has run.

## Decision rule

Reject a claimed migration benefit if coverage cannot be identified, rollback cannot be demonstrated, or the deployment violates required reliability. If baseline platforms provide the same benefit with lower total integration burden, revise the commercial thesis toward platform delivery rather than a separate product.
