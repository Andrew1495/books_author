from db.run_sql import run_sql
from models.author import Author
from models.book import Book
from repositories import author_repo


def save(book):
    sql = "INSERT INTO books (title, genre, author_id) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title , book.genre, book.author.id ]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book


def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def select_by_id(id):
    author = None
    sql = "SELECT FROM books WHERE ID = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repo.select_by_id(result['author_id'])
        book = Book(result["title"], author, result["genre"], result["id"] )
    return book

    

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repo.select_by_id(row['author_id'])
        book = Book(row["title"], author, row["genre"])
        books.append(book)
    return books

def update(book):
    sql = " UPDATE books SET (title, genre, author_id) = (%s, %s, %s) Where id = %s"
    values = [book.title, book.genre, book.author.id]
    run_sql(sql, values)

def delete_id(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
