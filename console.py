import pdb
import repositories.author_repo as author_repo
import repositories.book_repo as book_repo
from models.book import Book
from models.author import Author

# author_repo.delete_all()
# book_repo.delete_all()

author1 = Author("J.K Rowling")
author2 = Author("J.R.Tolkein")

author_repo.save(author1)
author_repo.save(author2)

book1 = Book("Harry Potter and the Goblet of Fire", author1, "Fantasy")
book2 = Book("The Lord of the Rings and The Fellowship of the Ring", author2, "Fantasy")
book3 = Book("Harry Potter and the Half-Blood Prince", author1, "Fantasy")
book4 = Book("The Lord of the Rings and The Two Towers", author2, "Fantasy")

book_repo.save(book1)
book_repo.save(book2)
book_repo.save(book3)
book_repo.save(book4)

print(book_repo.select_by_id(61))

