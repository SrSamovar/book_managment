from datetime import date

from pydantic import BaseModel

class AuthorBaseResponse(BaseModel):
    id: int

class AuthorCreateRequest(BaseModel):
    name: str
    birth_date: date


class AuthorCreateResponse(AuthorBaseResponse):
    pass


class AuthorUpdateRequest(BaseModel):
    name: str | None = None
    birth_date: date | None = None


class AuthorUpdateResponse(AuthorBaseResponse):
    pass
