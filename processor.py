import csv
import json
import os
from datetime import datetime, timezone

SUPPORTED_FORMATS = ['csv', 'tsv', 'json']

_AUDIT_LOG = os.path.join(os.path.dirname(__file__), 'logs', 'change_audit.jsonl')

def _audit(function_name, params):
    entry = {
        "function": function_name,
        "params": params,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "reason": "filter_applied",
    }
    os.makedirs(os.path.dirname(_AUDIT_LOG), exist_ok=True)
    with open(_AUDIT_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')

def load_data(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))

def save_output(data, path):
    if not data:
        return
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def filter_by_field(data, field, value):
    _audit("filter_by_field", {"field": field, "value": value})
    return [row for row in data if row.get(field) == value]

def filter_by_threshold(data, field, threshold):
    _audit("filter_by_threshold", {"field": field, "threshold": threshold})
    return [row for row in data if float(row.get(field, 0)) > threshold]

def transform_fields(data, mapping):
    _audit("transform_fields", {"mapping": mapping})
    result = []
    for row in data:
        new_row = {mapping.get(k, k): v for k, v in row.items()}
        result.append(new_row)
    return result

_AUDIT_LOG = os.path.join(os.path.dirname(__file__), 'logs', 'change_audit.jsonl')

def _audit(function_name, params):
    entry = {
        "function": function_name,
        "params": params,
        "timestamp": datetime.now().isoformat(),
        "reason": "filter_applied",
    }
    os.makedirs(os.path.dirname(_AUDIT_LOG), exist_ok=True)
    with open(_AUDIT_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')
