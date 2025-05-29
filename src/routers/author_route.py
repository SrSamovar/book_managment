from fastapi import APIRouter

from ..core.dependency import SessionDependency, AuthorDAODependency
from src.schemas import author
from ..services.author import AuthorService

author_router = APIRouter()


@author_router.get("/author/{author_id}", response_model=author.GetAuthorResponse)
async def get_author_by_id(author_id: int,
                           session: SessionDependency,
                           author_dao: AuthorDAODependency):
    query = AuthorService(author_dao)
    response = await query.get_author_by_id(session, author_id)
    result = author.GetAuthorResponse.model_validate(response)
    return result


@author_router.get("/authors", response_model=author.GetAuthorsListResponse)
async def get_authors(session: SessionDependency, author_dao: AuthorDAODependency):
    query = AuthorService(author_dao)
    results = await query.get_all_authors(session)
    return author.GetAuthorsListResponse(authors=[result.info for result in results])


@author_router.post("/author", response_model=author.AuthorCreateResponse)
async def create_author(session: SessionDependency,
                     author_dao: AuthorDAODependency,
                     author_data: author.AuthorCreateRequest):
    query = AuthorService(author_dao)
    result = await query.create_author(session, author_data)
    return {"id": result}


@author_router.patch("/author/{author_id}", response_model=author.AuthorUpdateResponse)
async def update_author(session: SessionDependency,
                        author_id: int,
                        author_data: author.AuthorUpdateRequest,
                        author_dao: AuthorDAODependency):
    query = AuthorService(author_dao)
    result = await query.update_author(session, author_id, author_data)
    return result


@author_router.delete("/author/{author_id}")
async def delete_author(session: SessionDependency, author_id: int, author_dao: AuthorDAODependency):
    query = AuthorService(author_dao)
    result = await query.delete_author(session, author_id)

    if result is True:
        return {"message": "Author deleted successfully"}

    return result
