"""json utils"""
import json


def beauty_dumps(data, indent=4, ensure_ascii=False):
    separators = (',', ': ')
    xdata = json.dumps(
        data,
        indent=indent,
        ensure_ascii=ensure_ascii,
        separators=separators
    )
    return xdata


def compress_dumps(data):
    xdata = json.dumps(
        data,
        ensure_ascii=False,
        separators=(',', ':')
    )
    return xdata
