from sqlalchemy.ext.asyncio import AsyncSession

from .base_service import BaseService
from ..daos.author_dao import AuthorDAO
from ..models import Author
from ..schemas.author import AuthorCreateRequest, AuthorUpdateRequest


class AuthorService(BaseService):
    """
    Класс автора для работы с DAO
    """
    def __init__(self, author_dao: AuthorDAO):
        super().__init__(author_dao)

    async def create_author(self, session: AsyncSession, request: AuthorCreateRequest) -> int:
        return await self.create_item(session, request)

    async def get_all_authors(self, session: AsyncSession) -> list[Author]:
        return await self.get_all_items(session)

    async def get_author_by_id(self, session: AsyncSession, author_id: int):
        return await self.get_item_by_id(session, author_id)

    async def delete_author(self, session: AsyncSession, author_id: int):
        return await self.delete_item(session, author_id)

    async def patch_author(self, session: AsyncSession,
                           author_id: int,
                           request: AuthorUpdateRequest):
        return await self.patch_item(session, author_id, request)
