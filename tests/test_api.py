import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.database import Base, engine


transport = ASGITransport(app=app)


@pytest.mark.asyncio
async def test_post_wallet_info(monkeypatch):
    # Очистка БД
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async def mock_get_wallet_info(address):
        from app.schemas import WalletInfo
        return WalletInfo(
            address=address,
            balance_trx=100.0,
            bandwidth=5000,
            energy=2000
        )

    monkeypatch.setattr("app.routes.get_wallet_info", mock_get_wallet_info)

    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/wallet-info", json={"address": "TValidAddress123"})
        assert response.status_code == 200
        data = response.json()
        assert data["balance_trx"] == 100.0
        assert data["bandwidth"] == 5000
        assert data["energy"] == 2000
