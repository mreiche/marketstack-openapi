from typing import List

from fastapi import APIRouter

from models import access_key_query, symbols_query, exchange_query, sort_query, Sort, Interval, limit_query, date_query, interval_query, date_path, Response, IntervalPrice, offset_query

router = APIRouter(prefix="/intraday", tags=["intraday"])


@router.get("", response_model=Response[List[IntervalPrice]], operation_id="intraday")
def query(
    access_key: str = access_key_query,
    symbols: str = symbols_query,
    exchange: str = exchange_query,
    sort: Sort = sort_query,
    interval: Interval = interval_query,
    date_from: str = date_query,
    date_to: str = date_query,
    limit: int = limit_query,
    offset: int = offset_query,
):
    pass


@router.get("/latest", response_model=Response[List[IntervalPrice]], operation_id="intraday_latest")
def latest(
    access_key: str = access_key_query,
    symbols: str = symbols_query,
    exchange: str = exchange_query,
    sort: Sort = sort_query,
    interval: Interval = interval_query,
    date_from: str = date_query,
    date_to: str = date_query,
    limit: int = limit_query,
    offset: int = offset_query,
):
    pass


@router.get("/{date}", response_model=Response[List[IntervalPrice]], operation_id="intraday_date")
def date(
    date: str = date_path,
    access_key: str = access_key_query,
    symbols: str = symbols_query,
    exchange: str = exchange_query,
    sort: Sort = sort_query,
    interval: Interval = interval_query,
    date_from: str = date_query,
    date_to: str = date_query,
    limit: int = limit_query,
    offset: int = offset_query,
):
    pass
