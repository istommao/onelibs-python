# onelibs document

## datetime utils


### get_datetime_from_ts

```python
from onelibs import dbutils

ts_str = 1618153215
dt_obj = dtutils.get_datetime_from_ts(ts_str)
print(dt_obj)

>>> datetime.datetime(2021, 4, 11, 23, 0, 15)
```


### get_datetime_str

```python
from onelibs import dbutils

ts_str = 1618153215
result = dtutils.get_datetime_str(ts_str)
print(result)

>>> 2021-04-11 23:00:15
```


### get_date_str

```python
from onelibs import dbutils

ts_str = 1618153215
result = dtutils.get_date_str(ts_str)
print(result)

>>> 2021-04-11
```


## get_time_str

```python
from onelibs import dbutils

ts_str = 1618153215
result = dtutils.get_time_str(ts_str)
print(result)

>>> 23:00:15
```

## get_today_remain_seconds


```python
from onelibs import dbutils

result = dtutils.get_today_remain_seconds()
```
