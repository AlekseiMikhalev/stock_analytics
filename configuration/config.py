from numpy import dot
from pydantic import BaseSettings
from datetime import date
import os
from dotenv import load_dotenv

load_dotenv()


class DataFetchingService(BaseSettings):
    application: str = 'Data Fetching Service'
    webmaster: str = 'mikhalev.aleksei1@gmail.com'
    created: date = '2023-03-20'
    data_source_api_config = {
        'session': True,
        'api_key': os.getenv('DATA_SOURCE_API_KEY')
    }
    database_url: str = os.getenv('DATABASE_URL')


class DataProcessingService(BaseSettings):
    application: str = 'Data Processing Service'
    webmaster: str = 'mikhalev.aleksei1@gmail.com'
    created: date = '2023-03-20'


class DataAnalyticsService(BaseSettings):
    application: str = 'Data Analytics Service'
    webmaster: str = 'mikhalev.aleksei1@gmail.com'
    created: date = '2023-03-20'


class ServerSettings(BaseSettings):
    production_server: str
    prod_port: int
    development_server: str
    dev_port: int

    class Config:
        env_file = os.getcwd() + '/configuration/stock_analytics.properties'
