"""test json utils"""
from onelibs import json_utils


def test_beauty_dumps():
    """test json beauty_dumps."""
    rawdata = {'hello': 'world'}
    result = json_utils.beauty_dumps(rawdata)
    assert result == '{\n    "hello": "world"\n}'


def test_compress_dumps():
    """test json compress_dumps."""
    rawdata = {'hello': 'world'}
    result = json_utils.compress_dumps(rawdata)
    assert result == '{"hello":"world"}'

