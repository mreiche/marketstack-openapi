from typing import List

from fastapi import APIRouter

from models import access_key_query, exchange_query, sort_query, Sort, limit_query, date_query, Response, EodPrice, search_query, symbol_path, Ticker, Split, IntervalPrice, Interval, interval_query, Dividend, date_path, offset_query

router = APIRouter(prefix="/tickers", tags=["tickers"])


@router.get("", response_model=Response[List[Ticker]], operation_id="tickers")
def query(
    access_key: str = access_key_query,
    exchange: str = exchange_query,
    search: str = search_query,
    limit: int = limit_query,
    offset: int = offset_query,
):
    pass


@router.get("/{symbol}", response_model=Ticker, operation_id="ticker_symbol")
def symbol(
    symbol: str = symbol_path,
    access_key: str = access_key_query,
):
    pass


class TickerEod(Ticker):
    eod: List[EodPrice]


@router.get(
    "/{symbol}/eod",
    response_model=Response[TickerEod],
    operation_id="ticker_symbol_eod"
)
def symbol_eod(
    symbol: str = symbol_path,
    access_key: str = access_key_query,
    exchange: str = exchange_query,
    sort: Sort = sort_query,
    date_from: str = date_query,
    date_to: str = date_query,
    limit: int = limit_query,
    offset: int = offset_query,
):
    pass


@router.get(
    "/{symbol}/eod/latest",
    response_model=EodPrice,
    operation_id="ticker_symbol_eod_latest"
)
def symbol_eod_latest(
    symbol: str = symbol_path,
    access_key: str = access_key_query,
):
    pass


@router.get(
    "/{symbol}/eod/{date}",
    response_model=EodPrice,
    operation_id="ticker_symbol_eod_date"
)
def symbol_eod_date(
    symbol: str = symbol_path,
    date: str = date_path,
    access_key: str = access_key_query,
):
    pass


class TickerIntraday(Ticker):
    intraday: List[IntervalPrice]


@router.get(
    "/{symbol}/intraday",
    response_model=Response[TickerIntraday],
    operation_id="ticker_symbol_intraday"
)
def symbol_intraday(
    symbol: str = symbol_path,
    access_key: str = access_key_query,
    exchange: str = exchange_query,
    sort: Sort = sort_query,
    interval: Interval | str = interval_query,
    date_from: str = date_query,
    date_to: str = date_query,
    limit: int = limit_query,
    offset: int = offset_query,
):
    pass


@router.get(
    "/{symbol}/intraday/latest",
    response_model=IntervalPrice,
    operation_id="ticker_symbol_intraday_latest"
)
def symbol_intraday_latest(
    symbol: str = symbol_path,
    access_key: str = access_key_query,
):
    pass


@router.get(
    "/{symbol}/intraday/{date}",
    response_model=Response[List[IntervalPrice]],
    operation_id="ticker_symbol_intraday_date"
)
def symbol_intraday_date(
    symbol: str = symbol_path,
    date: str = date_path,
    access_key: str = access_key_query,
):
    pass


@router.get(
    "/{symbol}/splits",
    response_model=Response[List[Split]],
    operation_id="ticker_symbol_splits"
)
def symbol_splits(
    symbol: str = symbol_path,
    access_key: str = access_key_query,
    sort: Sort = sort_query,
    date_from: str = date_query,
    date_to: str = date_query,
):
    pass


@router.get(
    "/{symbol}/dividends",
    response_model=Response[List[Dividend]],
    operation_id="ticker_symbol_dividends"
)
def symbol_dividends(
    symbol: str = symbol_path,
    access_key: str = access_key_query,
    sort: Sort = sort_query,
    date_from: str = date_query,
    date_to: str = date_query,
):
    pass
