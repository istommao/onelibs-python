"""onelibs datetime_utils."""
import datetime


def get_datetime_from_ts(timestamp: int) -> datetime.datetime:
    """Get datetime from timestamp."""
    result = datetime.datetime.fromtimestamp(timestamp)
    return result


def get_datetime_str(timestamp: int):
    """Get format datetime."""
    dt = get_datetime_from_ts(timestamp)
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def get_date_str(timestamp: int):
    """Get format date."""
    dt = get_datetime_from_ts(timestamp)
    return dt.strftime('%Y-%m-%d')


def get_time_str(timestamp: int):
    """Get format time."""
    dt = get_datetime_from_ts(timestamp)
    return dt.strftime('%H:%M:%S')


def get_today_max_ts():
    today = datetime.datetime.today()
    today_max = datetime.datetime.combine(today, datetime.time.max)
    today_max_ts = int(today_max.timestamp())
    return today_max_ts
