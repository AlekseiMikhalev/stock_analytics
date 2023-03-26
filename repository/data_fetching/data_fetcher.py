from typing import Dict, Any
from tiingo import TiingoClient

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from models.data.data_fetching_models import StockData
from configuration.config import DataFetchingService
import json

API_CONFIG = DataFetchingService().data_source_api_config


class DataFetcher:
    def __init__(self, sess: Session, api_config: dict = API_CONFIG) -> None:
        self.sess: Session = sess
        self.api_config = api_config

    async def fetch_stock_data(self, stock_symbol: str, *args, **kwargs):
        client = TiingoClient(self.api_config)
        dictionary = {}

        # Get ticker metadata
        ticker_metadata = client.get_ticker_metadata(stock_symbol)
        dictionary['TICKER_METADATA'] = ticker_metadata

        # Get latest prices, based on 3+ sources as JSON, sampled weekly
        ticker_price = client.get_ticker_price(
            stock_symbol, frequency="weekly")
        dictionary['TICKER_PRICE'] = ticker_price

        # Get historical GOOGL prices from August 2017 as JSON, sampled daily
        historical_prices = client.get_ticker_price(stock_symbol,
                                                    fmt='json',
                                                    startDate='2017-08-01',
                                                    endDate='2017-08-31',
                                                    frequency='daily')
        dictionary['TICKER_HISTORICAL_PRICES'] = historical_prices

        # # Get news articles about given tickers or search terms from given domains
        # TODO: News are not allowed in free version of Tiingo API
        # articles = client.get_news(tickers=[stock_symbol],
        #                            startDate='2017-01-01',
        #                            endDate='2017-08-31')

        # Get definitions for fields available in the fundamentals-api, ticker is
        # optional
        definitions = client.get_fundamentals_definitions(stock_symbol)
        dictionary['TICKER_DEFINITIONS'] = definitions

        # Get fundamentals which require daily-updated (like marketCap). A start-
        # and end-date can be passed. If omited, will get all available data.
        fundamentals_daily = client.get_fundamentals_daily(stock_symbol,
                                                           startDate='2021-01-01',
                                                           endDate='2021-12-31')
        dictionary['FUNDAMENTALS_DAILY'] = fundamentals_daily

        # Get fundamentals based on quarterly statements. Accepts time-range like
        # daily-fundamentals. asReported can be set to get the data exactly like
        # it was reported to SEC. Set to False if you want to get data containing
        # corrections
        fundamentals_stmnts = client.get_fundamentals_statements(stock_symbol,
                                                                 startDate='2020-01-01',
                                                                 endDate='2020-12-31',
                                                                 asReported=True)
        dictionary['FUNDAMENTALS_STMNTS'] = fundamentals_stmnts

        # convert dictionary to JSON string
        json_data = json.dumps(dictionary)

        # write the JSON string to a file
        with open('data.json', 'w') as f:
            f.write(json_data)

    async def insert_stock_data(self, stock_data: StockData) -> bool:
        try:
            sql = insert(StockData).values(symbol=stock_data.symbol,
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
        return q.scalar()
