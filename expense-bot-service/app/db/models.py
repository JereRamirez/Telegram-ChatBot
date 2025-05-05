from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Numeric

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, telegram_id={self.telegram_id})>"


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    description = Column(String, nullable=False)
    amount = Column(Numeric, nullable=False)
    category = Column(String, nullable=False)
    added_at = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return f"<Expense(id={self.id}, user_id={self.user_id}, amount={self.amount}, category={self.category})>"