# filteraudit

A lightweight Python utility for filtering and transforming CSV data.

## Usage

```python
from processor import load_data, filter_by_field, save_output
data = load_data("input.csv")
filtered = filter_by_field(data, "status", "active")
save_output(filtered, "output.csv")
```

## Setup

```bash
pip install pytest
```

## Tests

```bash
pytest tests/
```

## Supported formats

CSV and TSV input files are supported. JSON output coming soon.
