from datetime import date

from sqlalchemy import Integer, String, Date, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Book(Base):
    """
    Таблица книг в базе данных
    """
    __tablename__ = 'books'

    title: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String, nullable=False)
    release: Mapped[date] = mapped_column(Date, default=func.current_date())
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'), nullable=False)

    author: Mapped['Author'] = relationship('Author', back_populates='books')

    @property
    def info(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'release': self.release,
            'price': self.price,
            'author_id': self.author_id
        }
