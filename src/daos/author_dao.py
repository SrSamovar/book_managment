from .base_dao import BaseDAO
from ..models.author import Author

class AuthorDAO(BaseDAO[Author]):
    """
    Класс для работы с таблицей авторов
    """
    model = Author
