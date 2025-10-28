from fastapi import APIRouter, Query
from tradingagents.datasources.taiwan_twse import TaiwanTWSEDataSource

router = APIRouter(prefix="/api/twse", tags=["twse"])
ds = TaiwanTWSEDataSource()

@router.get("/daily_all")
def daily_all(date: str = Query(..., description="YYYY-MM-DD 或 YYYYMMDD")):
    df = ds.get_market_daily_all(date)
    return df.to_dict(orient="records")

@router.get("/stock_daily")
def stock_daily(
    symbol: str = Query(..., description="ex: 2330"),
    month: str = Query(..., description="YYYY-MM，例如 2025-09")
):
    df = ds.get_stock_daily(symbol, month)
    return df.to_dict(orient="records")

@router.get("/valuation")
def valuation(symbol: str = Query(..., description="ex: 2330")):
    df = ds.get_valuation_snapshot(symbol)
    return df.to_dict(orient="records")
