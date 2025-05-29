from datetime import date

from pydantic import BaseModel, ConfigDict, computed_field


class AuthorBaseResponse(BaseModel):
    id: int

class AuthorCreateRequest(BaseModel):
    name: str
    birth_date: date

    @computed_field
    def age(self) -> int:
        today = date.today()
        age = today.year - self.birth_date.year
        return int(age)


class AuthorCreateResponse(AuthorBaseResponse):
    pass


class AuthorUpdateRequest(BaseModel):
    name: str | None = None
    birth_date: date | None = None


class AuthorUpdateResponse(AuthorBaseResponse):
    pass


class GetAuthorResponse(AuthorBaseResponse):
    name: str
    birth_date: date
    age: int

    class Config:
        from_attributes = True


class GetAuthorsListResponse(BaseModel):
    authors: list[GetAuthorResponse] | None = None
