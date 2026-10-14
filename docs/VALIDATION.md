# Validation record — 3.0.0

Date: 2026-10-14.

## Completed development checks

- Official skill-creator quick validator: passed with UTF-8 mode. The first Windows run used the system code page and failed decoding typographic punctuation; rerunning with `PYTHONUTF8=1` passed. No validator rules were weakened.
- Portable plugin manifest: validated against the published Agent Plugins 1.0.0 JSON schema.
- Local checks: YAML/frontmatter, version consistency, reference paths, marketplace target, instruction-only file allowlist and common secret/local-path patterns.
- Validator rejection checks: malformed manifest, missing linked reference and private local path all rejected.
- GPT-6.1 Sol development evaluation: six fictional scenarios produced responses/action plans after reading the candidate. New-user intake, schedule change with timeout, job deduplication/partial coverage, interrupted Notion setup, urgent letter with embedded malicious instructions, and an unrelated non-trigger question were exercised. [Raw simulation evidence](behavior-check.md).
- Evaluation found no blocking defect in those simulations. Its scheduler-timeout clarification was implemented and two targeted recovery simulations passed on the revised candidate: update timeout with successful readback, and initial creation with unavailable lookup. Fit vocabulary was aligned to the shared Notion schema.
- Release ZIP: deterministic construction, archive integrity and byte-for-byte comparison against all ten runtime files passed. The release includes its SHA-256 checksum.
- Hosted CI was not activated: the GitHub connection lacks the workflow scope required to publish Actions files. Local automated validation passed; `docs/validate-workflow.yml.example` is supplied for an owner to place at `.github/workflows/validate.yml` using a suitably authorized connection.

## What these checks do not prove

The evaluator used development context and fictional tool outcomes, not a fresh recipient account or live tool execution. This is not independent acceptance, automatic routing measurement, a benchmark against v2, or proof of performance across future models.

Live ChatGPT ZIP import, Notion creation/permissions, unattended job scans, scheduler execution/notification delivery and document rendering were not tested. No author's personal Notion records or schedules were changed during development. GitHub source publication and release-asset integrity are checked separately at release.

## Recipient acceptance

1. Install the release ZIP in a supported account and select Career Optimizer in a fresh chat.
2. Complete the first intake steps without a CV; verify a private HQ and actual returned resource links.
3. Save and read back one real authorized Experience record; resume the chat without restarting setup.
4. Run a manual search with the recipient's constraints. Verify sources, deduplication and unknown handling.
5. If requested, create a daily or weekly task and inspect its active state/next run. Review the first unattended result.
6. Change/pause the actual task and verify it. Keep the Notion data through plugin updates.

Never treat the existence of this checklist as evidence those recipient checks have passed.
