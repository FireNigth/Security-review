# Example output (fictional)

### [Medium] Authenticated users can read another account's invoice

- **Location:** `mini-invoice-app.py:10-13`
- **Evidence:** The route requires a login, but it loads an invoice directly from the caller-supplied `invoice_id` and returns its data without checking that `invoice.owner_id` matches `current_user.id`.
- **Impact:** Any authenticated user who can guess or obtain another invoice ID may read its owner and total. This assumes invoice IDs are reachable and there is no ownership check in middleware or the data layer.
- **Recommendation:** Enforce ownership in the lookup (for example, query by both `invoice_id` and `current_user.id`) and return the same not-found response for records the caller cannot access.

This example demonstrates the desired evidence and uncertainty handling. The code is intentionally incomplete and is not a production application.
