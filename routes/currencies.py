from typing import List

from fastapi import APIRouter

from models import access_key_query, limit_query, Response, Currency

router = APIRouter(prefix="/currencies", tags=["currencies"])


@router.get("", response_model=Response[List[Currency]], operation_id="currencies")
def query(
    access_key: str = access_key_query,
    limit: int = limit_query,
    offset: int = limit_query,
):
    pass
