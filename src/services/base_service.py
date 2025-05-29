from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession


class BaseService:
    """
    Базовый класс для работы с DAO
    """

    def __init__(self, dao):
        self.dao = dao

    async def create_item(self, session: AsyncSession,
                          request_data) -> int:
        """
        Создание объекта в базе данных

        :param request_data:
        :param session: AsyncSession
        :return:
        """
        if request_data is None:
            raise HTTPException(status_code=400, detail='Введены не все данные')

        try:
            query = await self.dao.add(session, request_data)
        except HTTPException as err:
            raise HTTPException(status_code=400, detail=err.detail)

        return query

    async def get_all_items(self, session: AsyncSession):
        """
        Поиск всех объектов модели в базе данных

        :param session: AsyncSession
        :return:
        """
        results = await self.dao.get_all(session)

        if results is None:
            raise HTTPException(status_code=404, detail='Item  not found')

        return results

    async def get_item_by_id(self, session: AsyncSession, item_id: int):
        """
        Поиск объекта по ID

        :param item_id:
        :param session:
        :return:
        """
        result = await self.dao.get_by_id(session, item_id)

        if result is None:
            raise HTTPException(status_code=404, detail='Item not found')

        return result

    async def delete_item(self, session: AsyncSession, item_id: int):
        """
        Удаление объекта из базы данных

        :param session:
        :param item_id:
        :return:
        """
        result = await self.dao.delete(session, item_id)

        if result is None:
            raise HTTPException(status_code=404, detail='Item not found')

        return result

    async def patch_item(self, session: AsyncSession,
                         item_id: int,
                         item_data) -> int:
        """
        Частичное изменение объекта в базе данных

        :param item_id:
        :param session:
        :param item_data:
        :return:
        """
        result = await self.dao.patch(session, item_id, item_data)

        if result is Exception:
            raise HTTPException(status_code=404, detail='Item not found')

        if result is None:
            raise HTTPException(status_code=400, detail='Enter the updated data')

        return result
