from pydantic import BaseModel
from datetime import datetime


class DataFetchingReq(BaseModel):
    id: int
    symbol: str
    price: float
    volume: int
    date: datetime
