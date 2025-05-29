from fastapi import FastAPI

from ..models.base import init_orm, close_orm


async def lifespan(app: FastAPI):
    await init_orm()
    print('START')
    yield
    await close_orm()
    print('STOP')