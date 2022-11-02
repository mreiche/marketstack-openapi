from datetime import datetime
from enum import Enum
from typing import Generic, List, TypeVar

from fastapi import Path, Query
from pydantic import BaseModel
from pydantic.generics import GenericModel

R = TypeVar("R")


class Pagination(BaseModel):
    limit: int
    offset: int
    count: int
    total: int


class ErrorCode(Enum):
    invalid_access_key = "invalid_access_key"
    missing_access_key = "missing_access_key"
    function_access_restricted = "function_access_restricted"
    inactive_user = "inactive_user"
    https_access_restricted = "https_access_restricted"
    invalid_api_function = "invalid_api_function"
    not_found = "404_not_found"
    usage_limit_reached = "usage_limit_reached"
    rate_limit_reached = "rate_limit_reached"
    internal_error = "internal_error"
    validation_error = "validation_error"


class Error(BaseModel):
    code: ErrorCode
    message: str
    context: dict | None


class Response(GenericModel, Generic[R]):
    pagination: Pagination | None
    data: R | None
    error: Error | None


class Split(BaseModel):
    date: str
    symbol: str
    split_factor: float


class Dividend(BaseModel):
    date: str
    symbol: str
    dividend: float


class IntervalPrice(BaseModel):
    date: datetime
    symbol: str
    volume: float | None
    open: float
    close: float | None
    low: float
    high: float
    exchange: str
    last: float | None


class EodPrice(IntervalPrice):
    split_factor: float
    dividend: float
    adj_open: float
    adj_close: float
    adj_high: float
    adj_low: float
    adj_volume: float


class Interval(Enum):
    min1 = "1min"
    min5 = "5min"
    min10 = "10min"
    min30 = "30min"
    hour1 = "1hour"
    hour3 = "3hour"
    hour6 = "6hour"
    hour12 = "12hour"
    hour24 = "24hour"


class Sort(Enum):
    ASC = "ASC"
    DESC = "DESC"


class Currency(BaseModel):
    code: str
    name: str
    symbol: str | None
    symbol_native: str | None


class Timezone(BaseModel):
    timezone: str
    abbr: str
    abbr_dst: str


class Exchange(BaseModel):
    name: str
    acronym: str
    mic: str
    country: str
    country_code: str
    city: str
    website: str
    currency: Currency | None
    timezone: Timezone | None


class Ticker(BaseModel):
    name: str
    symbol: str
    stock_exchange: Exchange
    timezone: Timezone | None
    has_intraday: bool
    has_eod: bool


date_description = "Date in the formats %Y-%m-%d, %Y-%m-%d %H:%M:%S or ISO-8601 %Y-%m-%dT%H:%M:%S+%Z"

reference_time = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
formatted_reference_time = reference_time.isoformat()+"+0000"
symbol_path = Path(title="Symbol", example="AAPL")
date_path = Path(title="Timestamp", description=date_description, example=formatted_reference_time)
symbols_query = Query(None, title="Comma-separated symbols list", example="AAPL,AMZN")
date_query = Query(None, title="Timestamp", example=formatted_reference_time, description=date_description)
access_key_query = Query(title="API access key")
exchange_query = Query(None, title="Exchange MIC", example="XNAS")
search_query = Query(None, title="Search string")
interval_query = Query(None, title="Intraday interval", example=Interval.min5.value)
sort_query = Query(None, title="Date/time sort order", example=Sort.DESC.value)
limit_query = Query(None, ge=1, example=10, le=1000)
offset_query = Query(None, ge=0, example=0)
exchange_path = Path(title="Exchange MIC", example="XNAS")
