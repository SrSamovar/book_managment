from sqlalchemy.ext.asyncio import AsyncSession

from .base_service import BaseService
from ..daos.book_dao import BookDAO
from ..models import Book
from ..schemas.book import BookCreateRequest, BookUpdateRequest


class BookService(BaseService):
    """
    Класс книги для работы с DAO
    """
    def __init__(self, book_dao: BookDAO):
        super().__init__(book_dao)

    async def create_book(self, session: AsyncSession,
                          request: BookCreateRequest) -> int:
        return await self.create_item(session, request)

    async def get_all_books(self, session: AsyncSession) -> list[Book]:
        return await self.get_all_items(session)

    async def get_book_by_id(self, session: AsyncSession,
                             book_id: int):
        return await self.get_item_by_id(session, book_id)

    async def delete_book(self, session: AsyncSession,
                          book_id: int):
        return await self.delete_item(session, book_id)

    async def update_book(self, session: AsyncSession,
                         book_id: int,
                         request: BookUpdateRequest):
        return await self.patch_item(session, book_id, request)