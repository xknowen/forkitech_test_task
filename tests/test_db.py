import os
import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.models import WalletQuery, Base


DATABASE_TEST_URL = os.getenv("DATABASE_TEST_URL", "postgresql+asyncpg://postgres:postgres@test_db:5432/test_db")


@pytest.mark.asyncio
async def test_insert_wallet_query():
    engine = create_async_engine(DATABASE_TEST_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        wallet = WalletQuery(address="TTestAddress123")
        session.add(wallet)
        await session.commit()

        result = await session.execute(
            select(WalletQuery).where(WalletQuery.address == "TTestAddress123")
        )
        row = result.scalar_one_or_none()

        assert row is not None
        assert row.address == "TTestAddress123"

    await engine.dispose()
