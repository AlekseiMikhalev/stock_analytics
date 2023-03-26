from pydantic import BaseModel
from datetime import datetime


class InsertDataReq(BaseModel):
    symbol: str
    price: float
    volume: int
    date: datetime


class DataFetchingReq(InsertDataReq):
    id: int
