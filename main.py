from contextlib import asynccontextmanager
from utils import make_consumer
from fastapi import FastAPI
from config import Settings



@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = Settings()
    print(1)
    await make_consumer(settings=settings)
    yield
  

app = FastAPI(lifespan=lifespan)


