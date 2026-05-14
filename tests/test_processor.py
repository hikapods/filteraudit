import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import pytest
from processor import load_data, save_output

def test_load_and_save_roundtrip(tmp_path):
    csv_file = tmp_path / "input.csv"
    csv_file.write_text("name,value\nalice,1\nbob,2\n")
    out_file = tmp_path / "output.csv"
    data = load_data(str(csv_file))
    save_output(data, str(out_file))
    result = load_data(str(out_file))
    assert result == data

def test_load_data_returns_list(tmp_path):
    csv_file = tmp_path / "input.csv"
    csv_file.write_text("name,value\nalice,1\n")
    result = load_data(str(csv_file))
    assert isinstance(result, list)
    assert len(result) == 1
