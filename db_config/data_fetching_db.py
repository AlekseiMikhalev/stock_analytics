from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from configuration.config import DataFetchingService

DB_URL = DataFetchingService().database_url

engine = create_async_engine(DB_URL, future=True, echo=True)
AsyncSessionFactory = sessionmaker(
    engine, expire_on_commit=False, autoflush=False, class_=AsyncSession)
Base = declarative_base()
