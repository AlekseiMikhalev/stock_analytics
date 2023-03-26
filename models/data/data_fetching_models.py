from sqlalchemy import Column, Integer, String, Float, DateTime
from db_config.data_fetching_db import Base


class StockData(Base):
    __tablename__ = 'stock_data'

    id = Column(Integer, primary_key=True, index=True,
                autoincrement=True, unique=True)
    symbol = Column(String, unique=True, index=True)
    price = Column(Float)
    volume = Column(Integer)
    date = Column(DateTime(timezone=True))
