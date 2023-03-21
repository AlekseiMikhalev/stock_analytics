from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URL = 'postgresql+asyncpg://test:test@localhost:5432/stocks'
engine = create_async_engine(DB_URL, future=True, echo=True)
AsynSessionFactory = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()


# async def init_models():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)


# async def get_session() -> AsyncSession:
#     async with async_session() as session:
#         yield session