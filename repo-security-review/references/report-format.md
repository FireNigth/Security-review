# Review report format

Use the user's language. Keep the report proportionate to the review; do not pad it with generic security advice.

## Findings

For each confirmed issue, use this shape:

### [Severity] Concise, specific title

- **Location:** `path/to/file.ext:line`
- **Evidence:** Describe the code path and relevant untrusted input or missing check. Include only a short snippet when needed to make the evidence clear.
- **Impact:** State what an attacker could achieve and the preconditions.
- **Recommendation:** Give a direct remediation direction.

Order findings from highest to lowest severity. Redact secret values. Report uncertainty explicitly rather than presenting a hypothesis as fact.

## Scope and limitations

State what was reviewed (for example, changed files, authentication flow, deployment configuration) and any material area that could not be evaluated. Mention that static review cannot establish runtime behavior where that matters.

## No findings

If none are substantiated, say: “No substantiated security findings in the reviewed scope.” Then state the inspected scope and important limitations. Do not imply that no vulnerabilities exist.
