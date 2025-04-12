from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import SessionLocal
from app.schemas import WalletRequest, WalletInfo
from app.tron import get_wallet_info
from app.models import WalletQuery


router = APIRouter()


async def get_db():
    async with SessionLocal() as session:
        yield session


@router.post("/wallet-info", response_model=WalletInfo)
async def fetch_wallet_info(request: WalletRequest, db: AsyncSession = Depends(get_db)):
    try:
        info = await get_wallet_info(request.address)
        db.add(WalletQuery(address=request.address))
        await db.commit()
        return info
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/wallet-info")
async def get_wallet_queries(limit: int = 10, offset: int = 0, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WalletQuery).order_by(WalletQuery.timestamp.desc()).limit(limit).offset(offset))
    queries = result.scalars().all()
    return [
        {
            "address": q.address,
            "timestamp": q.timestamp.isoformat()
        } for q in queries
    ]
