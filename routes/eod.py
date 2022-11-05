from typing import List

from fastapi import APIRouter

from models import access_key_query, symbols_query, exchange_query, sort_query, Sort, limit_query, date_query, date_path, PagedResponse, EodPrice, offset_query

router = APIRouter(prefix="/eod", tags=["eod"])


@router.get("", response_model=PagedResponse[List[EodPrice]], operation_id="eod")
def query(
    access_key: str = access_key_query,
    symbols: str = symbols_query,
    exchange: str = exchange_query,
    sort: Sort = sort_query,
    date_from: str = date_query,
    date_to: str = date_query,
    limit: int = limit_query,
    offset: int = offset_query,
):
    pass


@router.get("/latest", response_model=PagedResponse[List[EodPrice]], operation_id="eod_latest")
def latest(
    access_key: str = access_key_query,
    symbols: str = symbols_query,
    exchange: str = exchange_query,
    sort: Sort = sort_query,
    date_from: str = date_query,
    date_to: str = date_query,
    limit: int = limit_query,
    offset: int = offset_query,
):
    pass


@router.get("/{date}", response_model=PagedResponse[List[EodPrice]], operation_id="eod_date")
def date(
    date: str = date_path,
    access_key: str = access_key_query,
    symbols: str = symbols_query,
    exchange: str = exchange_query,
    sort: Sort = sort_query,
    date_from: str = date_query,
    date_to: str = date_query,
    limit: int = limit_query,
    offset: int = offset_query,
):
    pass
