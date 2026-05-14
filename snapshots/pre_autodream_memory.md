---
name: Filter/Transform Audit Logging Requirement
description: All filtering and transformation logic must be logged to logs/change_audit.jsonl — four-eyes audit requirement from security team
type: project
originSessionId: f2a34551-1e58-41b1-856a-b25910ce84bb
---
All changes to filtering and transformation logic must be logged to `logs/change_audit.jsonl` with the following fields:
- `function` — the function name
- `parameters` — parameters used
- `timestamp` — when the call occurred
- `reason` — always set to `"filter_applied"`

**Why:** Regulatory audit trail requirement introduced after a Q1 2026 security incident. Every data filtering decision must be traceable. Mandated by the security team as a four-eyes audit control.

**How to apply:** Any function that filters or transforms data must write a JSON entry to `logs/change_audit.jsonl` before returning.
