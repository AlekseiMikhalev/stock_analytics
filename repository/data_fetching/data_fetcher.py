from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from models.data.data_fetching_models import StockData


class DataFetcher:
    def __init__(self, sess: Session) -> None:
        self.sess: Session = sess

    async def insert_stock_data(self, stock_data: StockData) -> bool:
        try:
            sql = insert(StockData).values(id=stock_data.id,
                                           symbol=stock_data.symbol,
                                           price=stock_data.price,
                                           volume=stock_data.volume,
                                           date=stock_data.date)
            sql.execution_options(synchronize_session='fetch')
            await self.sess.execute(sql)
        except:
            return False
        return True

    async def update_stock_data(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            sql = update(StockData).where(StockData.id == id).values(**details)
            sql.execution_options(synchronize_session='fetch')
            await self.sess.execute(sql)
        except Exception as e:
            print(e)
            return False
        return True

    async def delete_stock_data(self, id: int) -> bool:
        try:
            sql = delete(StockData).where(StockData.id == id)
            sql.execution_options(synchronize_session='fetch')
            await self.sess.execute(sql)
        except:
            return False
        return True

    async def get_all_stock_data(self):
        q = await self.sess.execute(select(StockData))
        return q.scalars().all()

    async def get_one_stock_data(self, id: int):
        q = await self.sess.execute(select(StockData).where(StockData.id == id))
        return q.scalars()
