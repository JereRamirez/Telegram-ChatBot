import sys
from loguru import logger

logger.remove()  # Remove default handler
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="DEBUG"
)

logger.add(
    "logs/bot_service.log",
    rotation="10 MB",
    retention="1 week",
    compression="zip",
    level="INFO"
)