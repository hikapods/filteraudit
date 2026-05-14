import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import pytest
from processor import load_data, filter_by_field, filter_by_threshold, transform_fields

def test_filter_by_field():
    data = [{"type": "A", "val": "1"}, {"type": "B", "val": "2"}]
    assert filter_by_field(data, "type", "A") == [{"type": "A", "val": "1"}]

def test_filter_by_threshold():
    data = [{"score": "10"}, {"score": "3"}, {"score": "7"}]
    result = filter_by_threshold(data, "score", 5)
    assert len(result) == 2

def test_transform_fields():
    data = [{"old_name": "x"}]
    result = transform_fields(data, {"old_name": "new_name"})
    assert result == [{"new_name": "x"}]

def test_filter_by_field_no_match():
    data = [{"type": "A"}]
    assert filter_by_field(data, "type", "Z") == []
