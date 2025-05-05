from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger
from decimal import Decimal
from datetime import datetime

from app.db.models import User, Expense
from app.db.database import get_db_session


class UserRepository:
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def get_by_telegram_id(self, telegram_id: str) -> User:
        logger.debug(f"Fetching user with telegram_id: {telegram_id}")
        result = await self.session.execute(select(User).where(User.telegram_id == telegram_id))
        return result.scalars().first()


class ExpenseRepository:
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(self, user_id: int, description: str, amount: float, category: str, added_at: datetime) -> Expense:
        expense = Expense(
            user_id=user_id,
            description=description,
            amount=Decimal(str(amount)),
            category=category,
            added_at=added_at
        )

        self.session.add(expense)
        await self.session.commit()
        await self.session.refresh(expense)

        return expense