from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from models import access_key_query, sort_query, Sort, limit_query, date_query, PagedResponse, EodPrice, search_query, IntervalPrice, Interval, interval_query, date_path, Exchange, exchange_path, symbols_query, offset_query, ExchangeBase

router = APIRouter(prefix="/exchanges", tags=["exchanges"])


@router.get("", response_model=PagedResponse[List[Exchange]], operation_id="exchanges")
def query(
    access_key: str = access_key_query,
    search: str = search_query,
    limit: int = limit_query,
    offset: int = offset_query,
):
    pass


@router.get("/{mic}", response_model=Exchange, operation_id="exchange_mic")
def mic(
    mic: str = exchange_path,
    access_key: str = access_key_query,
):
    pass


class ExchangeSymbol(BaseModel):
    name: str
    symbol: str
    has_intraday: bool
    has_eod: bool


class ExchangeTickers(ExchangeBase):
    tickers: List[ExchangeSymbol]


@router.get(
    "/{mic}/tickers",
    response_model=PagedResponse[ExchangeTickers],
    operation_id="exchange_mic_tickers"
)
def tickers(
    mic: str = exchange_path,
    access_key: str = access_key_query,
):
    pass


class ExchangeEod(ExchangeBase):
    eod: List[EodPrice]


@router.get(
    "/{mic}/eod",
    response_model=PagedResponse[ExchangeEod],
    operation_id="exchange_mic_eod"
)
def mic_eod(
    mic: str = exchange_path,
    access_key: str = access_key_query,
    symbols: str = symbols_query,
    sort: Sort = sort_query,
    date_from: str = date_query,
    date_to: str = date_query,
    limit: int = limit_query,
    offset: int = offset_query,
):
    pass


@router.get(
    "/{mic}/eod/latest",
    response_model=PagedResponse[ExchangeEod],
    operation_id="exchange_mic_eod_latest"
)
def mic_eod_latest(
    mic: str = exchange_path,
    access_key: str = access_key_query,
    symbols: str = symbols_query,
):
    pass


@router.get(
    "/{mic}/eod/{date}",
    response_model=PagedResponse[ExchangeEod],
    operation_id="exchange_mic_eod_date"
)
def mic_eod_date(
    mic: str = exchange_path,
    date: str = date_path,
    symbols: str = symbols_query,
    access_key: str = access_key_query,
):
    pass


class ExchangeIntraday(ExchangeBase):
    intraday: List[IntervalPrice]


@router.get(
    "/{mic}/intraday",
    response_model=PagedResponse[ExchangeIntraday],
    operation_id="exchange_mic_intraday"
)
def mic_intraday(
    mic: str = exchange_path,
    access_key: str = access_key_query,
    symbols: str = symbols_query,
    interval: Interval = interval_query,
    sort: Sort = sort_query,
    date_from: str = date_query,
    date_to: str = date_query,
    limit: int = limit_query,
    offset: int = offset_query,
):
    pass


@router.get(
    "/{mic}/intraday/latest",
    response_model=PagedResponse[ExchangeIntraday],
    operation_id="exchange_mic_intraday_latest"
)
def mic_intraday_latest(
    mic: str = exchange_path,
    symbols: str = symbols_query,
    access_key: str = access_key_query,
):
    pass


@router.get(
    "/{mic}/intraday/{date}",
    response_model=PagedResponse[ExchangeIntraday],
    operation_id="exchange_mic_intraday_date"
)
def mic_intraday_date(
    mic: str = exchange_path,
    date: str = date_path,
    symbols: str = symbols_query,
    access_key: str = access_key_query,
):
    pass
