from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.daos.author_dao import AuthorDAO
from src.daos.book_dao import BookDAO
from src.models.base import async_session_maker


async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session


SessionDependency = Annotated[AsyncSession, Depends(get_session)]


async def get_author_dao() -> AuthorDAO:
    return AuthorDAO()


AuthorDAODependency = Annotated[AuthorDAO, Depends(get_author_dao)]


async def get_book_dao() -> BookDAO:
    return BookDAO()


BookDAODependency = Annotated[BookDAO, Depends(get_book_dao)]
