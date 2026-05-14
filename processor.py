import csv
import json
import os
from datetime import datetime

SUPPORTED_FORMATS = ['csv', 'tsv', 'json']

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
