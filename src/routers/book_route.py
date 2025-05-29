from fastapi import APIRouter

from ..core.dependency import SessionDependency, BookDAODependency
from ..schemas import book
from ..services.book import BookService


book_router = APIRouter()


@book_router.get('book/{book_id}', response_model=book.GetBookResponse)
async def get_book_by_id(session: SessionDependency,
                         book_id: int,
                         book_dao: BookDAODependency):
    query = BookService(book_dao)
    results = await query.get_book_by_id(session, book_id)
    return results


@book_router.get('books/', response_model=book.GetBooksListResponse)
async def get_books(session: SessionDependency, book_dao: BookDAODependency):
    query = BookService(book_dao)
    results = await query.get_all_books(session)
    return book.GetBooksListResponse(books=[result.info for result in results])


@book_router.post('book/', response_model=book.BookCreateResponse)
async def create_book(session: SessionDependency,
                      book_data: book.BookCreateRequest,
                      book_dao: BookDAODependency):
    query = BookService(book_dao)
    results = await query.create_book(session, book_data)
    return {'id': results}


@book_router.patch('book/{book_id}', response_model=book.BookUpdateResponse)
async def update_book(session: SessionDependency,
                      book_data: book.BookUpdateRequest,
                      book_id: int,
                      book_dao: BookDAODependency):
    query = BookService(book_dao)
    results = await query.update_book(session, book_id, book_data)
    return results


@book_router.delete('/book/{book_id}')
async def delete_book(session: SessionDependency,
                      book_id: int,
                      book_dao: BookDAODependency):
    query = BookService(book_dao)
    result = await query.delete_book(session, book_id)

    if result is True:
        return {"message": "Book deleted successfully"}
    return result
