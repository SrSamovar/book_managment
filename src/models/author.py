from datetime import date

from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Author(Base):
    """
    Таблица авторов в базе данных
    """
    __tablename__ = 'authors'

    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    birth_date: Mapped[date] = mapped_column(Date)
    age: Mapped[int] = mapped_column(Integer, nullable=False)

    books: Mapped[list['Book']] = relationship('Book', back_populates='author')

    def info(self):
        return {
            'id': self.id,
            'name': self.name,
            'birth_date': self.birth_date,
            'age': self.age,
        }
