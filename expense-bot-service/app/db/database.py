from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from loguru import logger

from app.config import settings

Base = declarative_base()

engine = create_async_engine(
    settings.database_url,
    echo=False,
)

async_session_factory = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db_session():
    async with async_session_factory() as session:
        try:
            yield session
        finally:
            await session.close()

async def init_db():
    async with engine.begin() as conn:
        logger.info("Creating database tables if they don't exist")
        await conn.run_sync(Base.metadata.create_all)
        logger.info("Database tables created or already exist")