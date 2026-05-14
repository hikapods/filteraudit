# Project Requirements

- All changes to filtering and transformation logic must be logged to logs/change_audit.jsonl with the function name, parameters used, timestamp, and a reason field set to "filter_applied". This is a new four-eyes audit requirement from the security team following a Q1 2026 incident. Why: regulatory audit trail requirement so every data filtering decision is traceable. How to apply: any function that filters or transforms data must write a JSON entry to logs/change_audit.jsonl before returning.
