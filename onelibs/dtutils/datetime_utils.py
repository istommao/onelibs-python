"""onelibs datetime_utils."""
import time
import datetime


def get_date_from_str(date_str: str, fmt='%Y-%m-%d') -> datetime.datetime:
    """Get datetime from str"""
    return datetime.datetime.strptime(date_str, fmt).date()


def get_datetime_from_str(datetime_str: str, fmt='%Y-%m-%d %H:%M:%S') -> datetime.datetime:
    """Get datetime from str"""
    return datetime.datetime.strptime(datetime_str, fmt)


def get_datetime_from_ts(timestamp: int) -> datetime.datetime:
    """Get datetime from timestamp."""
    result = datetime.datetime.fromtimestamp(timestamp)
    return result


def get_datetime_str(timestamp: int, fmt='%Y-%m-%d %H:%M:%S'):
    """Get format datetime."""
    return get_datetime_from_ts(timestamp).strftime(fmt)


def get_date_str(timestamp: int, fmt='%Y-%m-%d'):
    """Get format date."""
    return get_datetime_from_ts(timestamp).strftime(fmt)


def get_time_str(timestamp: int, fmt='%H:%M:%S'):
    """Get format time."""
    return get_datetime_from_ts(timestamp).strftime(fmt)


def get_today_max_ts():
    """Get today max ts."""
    today = datetime.datetime.today()
    today_max = datetime.datetime.combine(today, datetime.time.max)

    today_max_ts = int(today_max.timestamp())
    return today_max_ts


def get_today_remain_seconds():
    """Get today remain seconds"""
    return 86400 - int(time.time()) % 86400
