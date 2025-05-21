from datetime import date

from pydantic import BaseModel


class BookBaseResponse(BaseModel):
    id: int


class BookCreateRequest(BaseModel):
    title: str
    description: str
    release_date: date
    price: int
    author_id : int


class BookCreateResponse(BookBaseResponse):
    pass


class BookUpdateRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    release_date: date | None = None
    price: int | None = None


class BookUpdateResponse(BookBaseResponse):
    pass
