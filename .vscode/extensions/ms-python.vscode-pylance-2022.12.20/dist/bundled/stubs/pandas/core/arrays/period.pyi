from typing import Sequence

import numpy as np
from pandas.core.arrays.datetimelike import (
    DatelikeOps,
    DatetimeLikeArrayMixin,
)

from pandas._libs.tslibs import Timestamp
from pandas._libs.tslibs.period import Period as Period

from pandas.tseries.offsets import Tick as Tick

class PeriodArray(DatetimeLikeArrayMixin, DatelikeOps):
    __array_priority__: int = ...
    def __init__(self, values, freq=..., dtype=..., copy: bool = ...) -> None: ...
    def dtype(self): ...
    def __array__(self, dtype=...) -> np.ndarray: ...
    def __arrow_array__(self, type=...): ...
    year: int = ...
    month: int = ...
    day: int = ...
    hour: int = ...
    minute: int = ...
    second: int = ...
    weekofyear: int = ...
    week: int = ...
    dayofweek: int = ...
    weekday: int = ...
    dayofyear: int = ...
    day_of_year = ...
    quarter: int = ...
    qyear: int = ...
    days_in_month: int = ...
    daysinmonth: int = ...
    @property
    def is_leap_year(self) -> bool: ...
    @property
    def start_time(self) -> Timestamp: ...
    @property
    def end_time(self) -> Timestamp: ...
    def to_timestamp(self, freq: str | None = ..., how: str = ...) -> Timestamp: ...
    def asfreq(self, freq: str | None = ..., how: str = ...) -> Period: ...
    def astype(self, dtype, copy: bool = ...): ...

def raise_on_incompatible(left, right): ...
def period_array(
    data: Sequence[Period | None],
    freq: str | Tick | None = ...,
    copy: bool = ...,
) -> PeriodArray: ...
def validate_dtype_freq(dtype, freq): ...
def dt64arr_to_periodarr(data, freq, tz=...): ...