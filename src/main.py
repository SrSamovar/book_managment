from fastapi import FastAPI

from src.core.lifespan import lifespan
from src.routers.author_route import author_router
from src.routers.book_route import book_router

app = FastAPI(
    lifespan=lifespan
)


app.include_router(author_router, tags=["author"], prefix='/api/v1')
app.include_router(book_router, tags=["book"], prefix='/api/v1')
