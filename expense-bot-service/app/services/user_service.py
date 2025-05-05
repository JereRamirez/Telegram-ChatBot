from fastapi import Depends
from loguru import logger

from app.db.repositories import UserRepository
from app.utils.exceptions import UserNotFoundError


class UserService:
    def __init__(self, user_repository: UserRepository = Depends()):
        self.user_repository = user_repository

    async def get_user_by_telegram_id(self, telegram_id: str):
        logger.debug(f"Getting user with telegram_id: {telegram_id}")
        user = await self.user_repository.get_by_telegram_id(telegram_id)

        if not user:
            logger.warning(f"User with telegram_id {telegram_id} not found")
            raise UserNotFoundError(f"User with telegram_id {telegram_id} not found")

        return user