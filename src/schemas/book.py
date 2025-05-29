from datetime import date

from pydantic import BaseModel, ConfigDict

from .author import GetAuthorResponse


class BookBaseResponse(BaseModel):
    id: int

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )


class BookCreateRequest(BaseModel):
    title: str
    description: str
    release: date
    price: int
    author_id : int


class BookCreateResponse(BookBaseResponse):
    pass


class BookUpdateRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    release: date | None = None
    price: int | None = None


class BookUpdateResponse(BookBaseResponse):
    pass


class GetBookResponse(BookBaseResponse):
    id: int
    title: str
    description: str
    release: date
    price: int
    author_id: int


class GetBooksListResponse(BaseModel):
    books: list[GetBookResponse]
