from .base_dao import BaseDAO
from ..models.book import Book

class BookDAO(BaseDAO[Book]):
    """
    Класс для работы с таблицой книг
    """
    model = Book