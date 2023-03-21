from fastapi import APIRouter, Depends
from configuration.config import DataFetchingService, ServerSettings
from db_config.data_fetching_db import AsynSessionFactory
from repository.data_fetching.data_fetcher import DataFetcher
from models.data.data_fetching_models import StockData
from models.request.data_fetching_request import DataFetchingReq


router = APIRouter()


def build_config():
    return DataFetchingService()


def fetch_config():
    return ServerSettings()


@router.get('/')
async def root(config: DataFetchingService = Depends(build_config),
               fconfig: ServerSettings = Depends(fetch_config)):
    return {'project_name': config.application,
            'webmaster': config.webmaster,
            'created': config.created,
            'development_server': fconfig.development_server,
            }


@router.post('/stock-data')
async def insert_stock_data(req: DataFetchingReq):
    async with AsynSessionFactory() as session:
        async with session.begin():
            data_fetcher = DataFetcher(session)
            stock_data = StockData(
                id=req.id,
                symbol=req.symbol,
                price=req.price,
                volume=req.volume,
                date=req.date
            )
            return await data_fetcher.insert_stock_data(stock_data)


@router.patch('/stock-data')
async def update_stock_data(id: int, req: DataFetchingReq):
    async with AsynSessionFactory() as session:
        async with session.begin():
            data_fetcher = DataFetcher(session)
            stock_data_dict = req.dict(exclude_unset=True)
            return await data_fetcher.update_stock_data(id, stock_data_dict)


@router.get('/stock-data/list')
async def list_stock_data():
    async with AsynSessionFactory() as session:
        async with session.begin():
            data_fetcher = DataFetcher(session)
            return await data_fetcher.get_all_stock_data()


@router.get('/stock-data/{id}')
async def get_one_stock_data(id: int):
    async with AsynSessionFactory() as session:
        async with session.begin():
            data_fetcher = DataFetcher(session)
            return await data_fetcher.get_one_stock_data(id)


@router.delete('/stock-data/{id}')
async def delete_stock_data(id: int):
    async with AsynSessionFactory() as session:
        async with session.begin():
            data_fetcher = DataFetcher(session)
            return await data_fetcher.delete_stock_data(id)
