from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from loguru import logger

from app.services.user_service import UserService
from app.services.expense_service import ExpenseService
from app.utils.exceptions import UserNotFoundError, ExpenseCategoryError

router = APIRouter()

class TelegramMessage(BaseModel):
    telegram_id: str
    message_text: str

class MessageResponse(BaseModel):
    response: str

@router.post("/message", response_model=MessageResponse)
async def process_message(
        message: TelegramMessage,
        user_service: UserService = Depends(),
        expense_service: ExpenseService = Depends()
):
    try:
        logger.info(f"Processing message from user {message.telegram_id}: {message.message_text}")

        # Validate user is in whitelist
        user = await user_service.get_user_by_telegram_id(message.telegram_id)

        # Categorize expense
        expense = await expense_service.categorize_expense(message.message_text)

        if expense is None:
            logger.warning(f"Skipping expense due to failed categorization for user {message.telegram_id}")
            return MessageResponse(response="")

        # Save expense to database
        await expense_service.add_expense(
            user_id=user.id,
            description=expense.description,
            amount=expense.amount,
            category=expense.category.name,
        )

        logger.info(f"Expense added for user {message.telegram_id}.")
        return MessageResponse(response=f"{expense.category.name} expense added ✅")

    except UserNotFoundError:
        logger.warning(f"User {message.telegram_id} not found in whitelist")
        return MessageResponse(response="")
    except ExpenseCategoryError as e:
        logger.warning(f"Error categorizing expense: {str(e)}")
        return MessageResponse(response="")
    except Exception as e:
        logger.error(f"Unexpected error processing message: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")