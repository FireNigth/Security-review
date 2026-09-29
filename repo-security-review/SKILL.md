---
name: repo-security-review
description: Review a code repository for actionable security weaknesses using static inspection, with evidence-based findings and practical remediation guidance. Use when asked to audit, review, or assess repository security; not for penetration testing or general feature reviews.
---

# Repo Security Review

Assess the requested repository or change set for concrete, exploitable security weaknesses. Produce a concise, prioritized review that a maintainer can verify and act on. Treat security as a review lens, not as permission to probe deployed systems or change code.

## Scope and boundaries

- Establish the requested scope: whole repository, selected paths, or a diff. Respect repository guidance such as `AGENTS.md` and avoid unrelated directories, generated files, and vendored code unless they are in scope.
- Use static inspection by default: read source, configuration, dependency manifests/lockfiles, and relevant diffs. Use local search and language-aware tooling already available when it materially helps.
- Do not run active scans against hosts, fuzz targets, exploit code, access external services, install packages, or execute application code as part of a review. Ask before an action would cross those boundaries.
- Do not modify files unless the user separately asks for fixes. Do not reproduce, print, or copy secret values; identify the file and secret type, and recommend rotation when a real credential appears committed.
- A risky API, dangerous function, or tool alert alone is not a finding. Trace attacker-controlled input to a security-sensitive operation and verify protections and reachable conditions.

## Review method

1. Map the entry points, trust boundaries, sensitive data, authorization checks, and security-relevant configuration inside scope.
2. Trace plausible attacker-controlled data into sensitive sinks, including database queries, shell/process invocation, filesystem paths, template or HTML output, deserialization, redirects, network fetches, and cryptographic operations.
3. Check access control and tenant boundaries at the operation itself; inspect authentication/session handling, input validation, output encoding, secrets, transport and storage settings, and dependency declarations where relevant.
4. For each candidate, verify the vulnerable path and look for mitigating controls. Follow data flow across files when needed. Drop candidates that depend on unsupported assumptions or lack concrete security impact.
5. Report only supported findings, ordered by severity. If none is substantiated, say so, describe the inspected scope, and mention material blind spots; do not claim the repository is secure.

## Finding quality

Each finding needs a short title with severity, exact file path and line (or smallest useful range), affected operation and attacker preconditions, concise impact and why existing controls do not stop it, and a practical remediation direction. Do not silently apply a fix.

Use `Critical`, `High`, `Medium`, `Low`, or `Informational`. Rate demonstrated impact and realistic reachability together; do not inflate severity because a weakness class sounds serious. Reserve `Critical` for severe, broadly exploitable compromise. State assumptions and uncertainty. Avoid duplicate findings for the same root cause. Never invent line numbers, exploitability, or affected versions.

Use the output structure in [references/report-format.md](references/report-format.md). Keep the main response focused on findings, then include concise scope and limitations. If a local tool result is uncertain, independently inspect the relevant code before reporting it.
