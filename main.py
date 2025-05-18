from contextlib import asynccontextmanager
from utils import consume_message
from fastapi import FastAPI
from config import Settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = Settings()
    print(1)
    await consume_message()
    yield


app = FastAPI(lifespan=lifespan)
