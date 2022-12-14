from typing import List

from fastapi import APIRouter

from models import access_key_query, symbols_query, sort_query, Sort, limit_query, date_query, PagedResponse, Split, offset_query

router = APIRouter(prefix="/splits", tags=["splits"])


@router.get("", response_model=PagedResponse[List[Split]], operation_id="splits")
def query(
    access_key: str = access_key_query,
    symbols: str = symbols_query,
    sort: Sort = sort_query,
    date_from: str = date_query,
    date_to: str = date_query,
    limit: int = limit_query,
    offset: int = offset_query,
):
    pass
