import json
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from models import responses

app = FastAPI(responses=responses)
from routes.eod import router as eod
from routes.intraday import router as intraday
from routes.splits import router as splits
from routes.dividends import router as dividends
from routes.currencies import router as currencies
from routes.timezones import router as timezones
from routes.tickers import router as tickers
from routes.exchanges import router as exchanges

app.include_router(eod)
app.include_router(intraday)
app.include_router(splits)
app.include_router(dividends)
app.include_router(currencies)
app.include_router(timezones)
app.include_router(tickers)
app.include_router(exchanges)

openapi_schema = get_openapi(
    title="Marketstack OpenAPI",
    version="1.0",
    description="Inofficial Marketstack OpenAPI spec",
    routes=app.routes,
)

with open("marketstack-openapi.json", "w") as file:
    json.dump(openapi_schema, file, indent=2)

#
# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi(
#         title="Custom title",
#         version="2.5.0",
#         description="This is a very custom OpenAPI schema",
#         routes=app.routes,
#     )
#     #openapi_schema["info"]["x-logo"] = {
#     #    "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
#     #}
#     app.openapi_schema = openapi_schema
#     return app.openapi_schema
