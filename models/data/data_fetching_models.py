from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db_config.data_fetching_db import Base


class StockData(Base):
    __tablename__ = 'stock_data'

    id = Column(Integer, primary_key=True, index=True,
                autoincrement=True, unique=True)
    symbol = Column(String, unique=True, index=True)
    price = Column(Float)
    volume = Column(Integer)
    date = Column(DateTime(timezone=True))


# class Company(Base):
#     __tablename__ = "COMPANY"
#     ticker = Column(String, primary_key=True)
#     name = Column(String)
#     description = Column(String)
#     startDate = Column(String)
#     endDate = Column(String)
#     exchangeCode = Column(String)
#     fundamentals = relationship("FundamentalsDaily", backref="company")
#     technicals = relationship("TickerPrice", backref="company")


# class TickerPrice(Base):
#     __tablename__ = "TICKER_PRICE"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     ticker = Column(String, ForeignKey("COMPANY.ticker"), nullable=False)
#     adjClose = Column(Float)
#     adjHigh = Column(Float)
#     adjLow = Column(Float)
#     adjOpen = Column(Float)
#     adjVolume = Column(Integer)
#     close = Column(Float)
#     date = Column(String)
#     divCash = Column(Float)
#     high = Column(Float)
#     low = Column(Float)
#     open = Column(Float)
#     splitFactor = Column(Float)
#     volume = Column(Integer)


# class TickerHistoricalPrices(Base):
#     __tablename__ = "TICKER_HISTORICAL_PRICES"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     ticker = Column(String, ForeignKey("COMPANY.ticker"), nullable=False)
#     adjClose = Column(Float)
#     adjHigh = Column(Float)
#     adjLow = Column(Float)
#     adjOpen = Column(Float)
#     adjVolume = Column(Integer)
#     close = Column(Float)
#     date = Column(String)
#     divCash = Column(Float)
#     high = Column(Float)
#     low = Column(Float)
#     open = Column(Float)
#     splitFactor = Column(Float)
#     volume = Column(Integer)


# class TickerDefinitions(Base):
#     __tablename__ = "TICKER_DEFINITIONS"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     ticker = Column(String, ForeignKey("COMPANY.ticker"), nullable=False)
#     dataCode = Column(String)
#     name = Column(String)
#     description = Column(String)
#     statementType = Column(String)
#     units = Column(String)


# class FundamentalsDaily(Base):
#     __tablename__ = "FUNDAMENTALS_DAILY"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     company_ticker = Column(String, ForeignKey(
#         "COMPANY.ticker"), nullable=False)
#     date = Column(String)
#     marketCap = Column(Float)
#     enterpriseVal = Column(Float)
#     peRatio = Column(Float)
#     pbRatio = Column(Float)
#     trailingPEG1Y = Column(Float)

# TODO: identify which items from financial statements need to be collected
# class FundamentalsStmts(Base):
#     __tablename__ = "FUNDAMENTALS_STMNTS"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     company_ticker = Column(String, ForeignKey(
#         "COMPANY.ticker"), nullable=False)
#     date = Column(String)
#     year = Column(Integer)
#     quarter = Column(Integer)
#     dataCode = Column(String)
#     value = Column(Float)
