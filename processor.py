import csv
import json
from datetime import datetime

def load_data(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))

def filter_by_field(data, field, value):
    return [row for row in data if row.get(field) == value]

def filter_by_threshold(data, field, threshold):
    results = []
    for row in data:
        try:
            if float(row.get(field, 0)) >= threshold:
                results.append(row)
        except (ValueError, TypeError):
            pass
    return results

def transform_fields(data, mapping):
    return [{mapping.get(k, k): v for k, v in row.items()} for row in data]

def save_output(data, path):
    if not data:
        return
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
