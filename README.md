# Repo Security Review

**An evidence-first security review skill for AI coding agents.** It helps an agent inspect a repository, trace security-sensitive data flows, and return a short, prioritized report with precise locations and practical remediation guidance.

This portfolio project is built around a simple principle: security findings should be reproducible from code evidence, not guesses from a list of scary function names.

## What it does

- Guides static reviews of source code, configuration, dependency manifests, and diffs.
- Emphasizes trust boundaries, authorization, untrusted input, and security-sensitive operations.
- Requires a location, attack preconditions, impact, and remediation direction for every finding.
- Encourages severity ratings based on demonstrated impact and realistic reachability.
- Keeps review read-only and distinguishes “no finding in scope” from “secure.”

## What it does not do

- Penetration testing, network scanning, exploitation, or fuzzing.
- Automatic code changes or package installation.
- Guarantee that a repository is free of vulnerabilities.

## Install in Codex

Copy the `repo-security-review` folder into your Codex skills directory:

```text
%USERPROFILE%\.codex\skills\repo-security-review\
```

Restart or refresh Codex if needed. Then ask for a security review of a repository or change set; Codex can select the skill automatically, or you can invoke `$repo-security-review` explicitly.

## Example request

> Review the authentication and account recovery code in this repository for security issues. Do not modify files. Report only findings you can support with code evidence.

See [a tiny intentionally flawed example](examples/mini-invoice-app.py) and [the matching illustrative report](examples/sample-review.md) to understand the expected level of evidence.

## Repository layout

```text
repo-security-review/       # Installable skill package
  SKILL.md                  # Skill entrypoint and review workflow
  agents/openai.yaml        # Codex UI metadata
  references/report-format.md
examples/                   # Small demonstration and sample output
```

## Design choices

The skill is intentionally tool-agnostic: the host agent uses the repository tools available to it. It favors source-level evidence and conservative claims over tool-specific checklists or unsupported risk labels. Reviews stay within the scope the user requested.

## English summary

Repo Security Review is a read-only, static code review skill for AI coding agents. It produces actionable findings with evidence, locations, impact, severity, and remediation guidance. It does not perform active testing or claim that a repository is vulnerability-free.
