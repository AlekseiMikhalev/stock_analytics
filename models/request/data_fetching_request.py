from pydantic import BaseModel
from datetime import datetime


class InsertDataReq(BaseModel):
    symbol: str
    price: float
    volume: int
    date: datetime


class DataFetchingReq(InsertDataReq):
    id: int



from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


# class TicketMetadata(BaseModel):
#     ticker: str
#     name: str
#     description: str
#     startDate: datetime
#     endDate: datetime
#     exchangeCode: str


# class TicketPrice(BaseModel):
#     adjClose: float
#     adjHigh: float
#     adjLow: float
#     adjOpen: float
#     adjVolume: int
#     close: float
#     date: datetime
#     divCash: float
#     high: float
#     low: float
#     open: float
#     splitFactor: float
#     volume: int


# class TicketHistoricalPrices(BaseModel):
#     date: datetime
#     close: float
#     high: float
#     low: float
#     open: float
#     volume: int
#     adjClose: float
#     adjHigh: float
#     adjLow: float
#     adjOpen: float
#     adjVolume: int
#     divCash: float
#     splitFactor: float


# class TicketDefinitions(BaseModel):
#     dataCode: str
#     name: str
#     description: str
#     statementType: str
#     units: str


# class FundamentalsDaily(BaseModel):
#     date: datetime
#     marketCap: float
#     enterpriseVal: float
#     peRatio: float
#     pbRatio: float
#     trailingPEG1Y: float


# class StatementData(BaseModel):
#     balanceSheet: List[dict]


# class FundamentalsStatements(BaseModel):
#     date: datetime
#     year: int
#     quarter: int
#     statementData: Optional[StatementData]


# class TicketData(BaseModel):
#     metadata: TicketMetadata
#     prices: List[TicketPrice]
#     historicalPrices: List[TicketHistoricalPrices]
#     definitions: List[TicketDefinitions]
#     fundamentalsDaily: List[FundamentalsDaily]
#     fundamentalsStatements: List[FundamentalsStatements]
