"""datetime utils tests"""
from onelibs.dtutils import datetime_utils


def test_get_datetime_from_ts():
    """GET datetime from ts."""
    ts_str = 1601452767

    dt_obj = datetime_utils.get_datetime_from_ts(ts_str)

    assert dt_obj.strftime('%Y-%m-%d %H:%M:%S') == '2020-09-30 15:59:27'


def test_get_datetime_str():
    """GET datetime str from ts."""
    ts_str = 1601452767

    result = datetime_utils.get_datetime_str(ts_str)

    assert result == '2020-09-30 15:59:27'


def test_get_date_str():
    """GET date str from ts."""
    ts_str = 1601452767

    result = datetime_utils.get_date_str(ts_str)

    assert result == '2020-09-30'


def test_get_time_str():
    """GET time str from ts."""
    ts_str = 1601452767

    result = datetime_utils.get_time_str(ts_str)

    assert result == '15:59:27'
