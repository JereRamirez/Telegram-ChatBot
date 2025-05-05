from langchain_google_genai import ChatGoogleGenerativeAI
from loguru import logger
from langchain_core.prompts import PromptTemplate

from app.config import settings
from pydantic import BaseModel, Field
from enum import Enum


class Category(Enum):
    HOUSING = 'housing'
    TRANSPORTATION = 'transportation'
    FOOD = 'food'
    UTILITIES = 'utilities'
    INSURANCE = 'insurance'
    MEDICAL = 'medical'
    SAVINGS = 'savings'
    DEBT = 'debt'
    EDUCATION = 'education'
    ENTERTAINMENT = 'entertainment'
    OTHER = 'other'


class Expense(BaseModel):
    category: Category = Field(..., description="The expense's category")
    amount: float = Field(..., description="The expense's amount")
    description: str = Field(..., description="The expense's description")
    error: str = Field(..., description="The expense's error")


class ExpenseCategorizer:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            google_api_key=settings.gemini_api_key,
            model="gemini-2.0-flash",
            temperature=0,
        ).with_structured_output(Expense)

        categories_str = ", ".join([e.value for e in Category])

        self.prompt_template = PromptTemplate.from_template(
            f'Your role is to categorize a text into one of the available categories. '
            f'If there is no amount mentioned or there is no expense in it add a description of what is missing in the error field.\n'
            f'## CATEGORIES ##\n'
            f'{categories_str}\n'
            f'## END OF CATEGORIES ##\n'
            f'## TEXT ##\n'
            f'{{text}}\n'
            f'## END OF TEXT ##'
        )

    async def categorize(self, description: str):
        try:
            response = await self.llm.ainvoke(self.prompt_template.format(text=description or ""))

            error = response.error.strip() if response.error else ""
            if error:
                logger.warning(f"LLM returned an error: {response.error}")
                return None

            logger.debug(f"Expense categorized into: {str(response)}")
            return response
        except Exception as e:
            logger.warning(f"Failed to categorize expense: {str(e)}")
            return None
