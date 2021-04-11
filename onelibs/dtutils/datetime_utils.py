"""onelibs datetime_utils."""
import time
import datetime

from functools import singledispatch


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


@singledispatch
def get_datetime_str(obj, fmt='%Y-%m-%d %H:%M:%S'):
    pass


@get_datetime_str.register(int)
def _(timestamp, fmt='%Y-%m-%d %H:%M:%S'):
    """Get datetime str from timestamp"""
    return get_datetime_from_ts(timestamp).strftime(fmt)


@get_datetime_str.register(datetime.datetime)
def _(dtobj, fmt='%Y-%m-%d %H:%M:%S'):
    """Get datetime str from datetime obj"""
    return dtobj.strftime(fmt)


@singledispatch
def get_date_str(obj, fmt='%Y-%m-%d'):
    pass


@get_date_str.register(int)
def _(timestamp, fmt='%Y-%m-%d') -> str:
    """Get date str from timestamp"""
    return get_datetime_from_ts(timestamp).strftime(fmt)


@get_date_str.register(datetime.datetime)
def _(dtobj, fmt='%Y-%m-%d') -> str:
    """Get date str from datetime obj"""
    return dtobj.strftime(fmt)


@get_date_str.register(datetime.date)
def _(dtobj, fmt='%Y-%m-%d') -> str:
    """Get date str from date obj"""
    return dtobj.strftime(fmt)


@singledispatch
def get_time_str(obj, fmt='%H:%M:%S'):
    pass


@get_time_str.register(datetime.datetime)
def _(dtobj, fmt='%H:%M:%S') -> str:
    """Get time str from datetime obj"""
    return dtobj.strftime(fmt)


@get_time_str.register(datetime.date)
def _(dtobj, fmt='%H:%M:%S') -> str:
    """Get time str from date obj"""
    return dtobj.strftime(fmt)


@get_time_str.register(int)
def _(timestamp, fmt='%H:%M:%S') -> str:
    """Get time str from timestamp obj"""
    return get_datetime_from_ts(timestamp).strftime(fmt)


def get_today_max_ts() -> int:
    """Get today max ts."""
    today = datetime.datetime.today()
    today_max = datetime.datetime.combine(today, datetime.time.max)

    today_max_ts = int(today_max.timestamp())
    return today_max_ts


def get_today_remain_seconds() -> int:
    """Get today remain seconds"""
    return 86400 - int(time.time()) % 86400


def get_start_of_today() -> datetime.datetime:
    """获取今天的开始时间."""
    return datetime.datetime.combine(datetime.date.today(), datetime.time.min)


def get_end_of_today() -> datetime.datetime:
    """获取今天的结束时间."""
    return datetime.datetime.combine(datetime.date.today(), datetime.time.max)


def get_last_month_range() -> tuple:
    """获取上个月"""
    end = datetime.date.today().replace(day=1) - datetime.timedelta(1)
    start = end.replace(day=1)
    return datetime.datetime.combine(start, datetime.time.min), datetime.datetime.combine(end, datetime.time.max)


def get_month_range(n) -> tuple:
    """获取第n个月"""
    today = datetime.date.today()
    year_diff = (today.month + n) // 12

    end = today.replace(
        month=(today.month + n) % 12 + 1,
        year=today.year + year_diff,
        day=1
    ) - datetime.timedelta(days=1)

    start = end.replace(day=1)
    return datetime.datetime.combine(start, datetime.time.min), datetime.datetime.combine(end, datetime.time.max)


def get_current_week():
    monday, sunday = datetime.date.today(), datetime.date.today()
    one_day = datetime.timedelta(days=1)

    while monday.weekday() != 0:
        monday -= one_day

    while sunday.weekday() != 6:
        sunday += one_day

    return monday, sunday
