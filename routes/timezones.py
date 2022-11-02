from typing import List

from fastapi import APIRouter

from models import access_key_query, limit_query, Response, Timezone

router = APIRouter(prefix="/timezones", tags=["timezones"])


@router.get("", response_model=Response[List[Timezone]], operation_id="timezones")
def query(
    access_key: str = access_key_query,
    limit: int = limit_query,
    offset: int = limit_query,
):
    pass
