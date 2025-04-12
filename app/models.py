from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.database import Base


class WalletQuery(Base):
    __tablename__ = "wallet_queries"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
