from contextlib import asynccontextmanager
from utils import consume_message
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(1)
    await consume_message()
    yield


app = FastAPI(lifespan=lifespan)
