import os
import asyncio
import asyncpg

from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv

from app.routes import router
from app.database import Base, engine


load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')


async def wait_for_postgres():
    while True:
        try:
            conn = await asyncpg.connect(DATABASE_URL.replace("+asyncpg", ""))
            await conn.close()
            print("✅ Подключение к PostgreSQL успешно")
            break
        except Exception as e:
            print(f"❌ Ошибка подключения: {e}")
            await asyncio.sleep(1)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await wait_for_postgres()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="Tron Wallet Info Service", lifespan=lifespan)
app.include_router(router)
