from typing import Generic, TypeVar

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.base import Base


T = TypeVar("T", bound=Base)

class BaseDAO(Generic[T]):
    """
    Базовый класс для работы с базой данных
    """
    model: type[T]

    @classmethod
    async def add(cls, session: AsyncSession, model: BaseModel) -> int:
        try:
            session.add(model)
            await session.commit()
            await session.refresh(model)
        except SQLAlchemyError as e:
            await session.rollback()
            err = str(e)
            raise err

        return model.id

    @classmethod
    async def get_all(cls, session: AsyncSession):
        try:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()
        except SQLAlchemyError as e:
            await session.rollback()
            err = str(e)
            raise err

    @classmethod
    async def get_by_id(cls, session: AsyncSession, item_id: int) -> dict | None:
        try:
            query = await session.get(cls.model, item_id)
            return query.info
        except SQLAlchemyError as e:
            err = str(e)
            raise err

    @classmethod
    async def delete(cls, session: AsyncSession, item_id: int) -> None:
        try:
            query = session.get(cls.model, item_id)
            await session.delete(query)
            await session.commit()
            await session.refresh(query)
        except SQLAlchemyError as e:
            await session.rollback()
            err = str(e)
            raise err

    @classmethod
    async def patch(cls, session: AsyncSession, item_id: int, item_data: BaseModel) -> int | None:
        item_dict = item_data.model_dump()
        try:
            req = session.get(cls.model, item_id)

            for key, value in item_dict.items():
                setattr(req, key, value)

            await session.commit()
            await session.refresh(req)
            return item_dict.id
        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            await session.rollback()
            err = str(e)
            raise err




