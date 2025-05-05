from fastapi import Depends
from datetime import datetime
from loguru import logger

from app.db.repositories import ExpenseRepository
from app.llm.expense_categorizer import ExpenseCategorizer


class ExpenseService:
    def __init__(self, expense_repository: ExpenseRepository = Depends(), expense_categorizer: ExpenseCategorizer = Depends()):
        self.expense_repository = expense_repository
        self.expense_categorizer = expense_categorizer

    async def add_expense(self, user_id: int, description: str, amount: float, category: str):
        logger.debug(f"Adding expense for user {user_id}: {description}, ${amount}, category: {category}")

        expense = await self.expense_repository.create(
            user_id=user_id,
            description=description,
            amount=amount,
            category=category,
            added_at=datetime.now()
        )

        logger.info(f"Expense added with ID: {expense.id}")
        return expense

    async def categorize_expense(self, description: str):
        logger.debug(f"Categorizing expense: {description}")
        return await self.expense_categorizer.categorize(description)