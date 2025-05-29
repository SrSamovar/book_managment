from typing import Generic, TypeVar

from fastapi import HTTPException
from pydantic import BaseModel, ValidationError
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
            model_data = model.model_dump(exclude_unset=True)
            request = cls.model(**model_data)
        except ValidationError as e:
            raise ValueError('Invalid data') from e

        try:
            session.add(request)
            await session.commit()
            await session.refresh(request)
        except SQLAlchemyError as e:
            await session.rollback()
            raise e

        return request.id

    @classmethod
    async def get_all(cls, session: AsyncSession):
        try:
            query = select(cls.model)
            result = await session.execute(query)

            if result is None:
                raise HTTPException(status_code=404, detail="Not found")

            return result.scalars().all()
        except HTTPException as e:
            raise
        except SQLAlchemyError as e:
            await session.rollback()
            err = str(e)
            raise err

    @classmethod
    async def get_by_id(cls, session: AsyncSession, item_id: int) -> dict | None:
        try:
            query = await session.get(cls.model, item_id)

            if query is None:
                raise HTTPException(status_code=404, detail="Item not found")

            return query.info
        except HTTPException as e:
            raise
        except SQLAlchemyError as e:
            err = str(e)
            raise err

    @classmethod
    async def delete(cls, session: AsyncSession, item_id: int) -> bool:
        try:
            query = await session.get(cls.model, item_id)

            if query is None:
                raise HTTPException(status_code=404, detail="Item not found")

            await session.delete(query)
            await session.commit()
            return True
        except HTTPException as e:
            raise
        except Exception as e:
            await session.rollback()
            raise SQLAlchemyError(f'Error deleting: {str(e)}') from e

    @classmethod
    async def patch(cls, session: AsyncSession, item_id: int, item_data: BaseModel) -> int | None:
        item_dict = item_data.model_dump(exclude_unset=True)
        try:
            req = await session.get(cls.model, item_id)

            for key, value in item_dict.items():
                setattr(req, key, value)

            await session.commit()
            await session.refresh(req)
            return req.info
        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            await session.rollback()
            err = str(e)
            raise err




