import pytest
from library_system.models.book import Book
from library_system.models.ebook import EBook
from library_system.models.audiobook import Audiobook
from library_system.models.author import Author
from library_system.models.borrower import Borrower

def test_book_creation():
    book = Book(resource_id="1", title="Python Basics", author="John Doe", isbn="12345", page_count=200)
    assert book.title == "Python Basics"
    assert book.page_count == 200
    assert "ISBN: 12345" in book.get_details()

def test_ebook_inheritance():
    ebook = EBook(
        resource_id="2", title="Advanced Python", author="Jane Doe", 
        isbn="67890", page_count=300, file_size_mb=1.5, file_format="PDF"
    )
    assert isinstance(ebook, Book)
    assert ebook.file_format == "PDF"
    assert "Size: 1.5 MB" in ebook.get_details()

def test_audiobook_inheritance():
    audiobook = Audiobook(
        resource_id="3", title="Python Audio", author="Jim Beam",
        isbn="11223", page_count=0, duration_minutes=120, narrator="Morgan Freeman"
    )
    assert audiobook.narrator == "Morgan Freeman"
    assert "Duration: 120 min" in audiobook.get_details()

def test_author_management():
    author = Author(name="J.K. Rowling")
    author.add_book("hp1")
    author.add_book("hp2")
    assert len(author.book_ids) == 2
    assert str(author) == "J.K. Rowling"

def test_borrower_operations():
    borrower = Borrower(name="Alice", email="alice@example.com")
    borrower.borrow_resource("book1")
    assert "book1" in borrower.borrowed_resource_ids
    
    borrower.return_resource("book1")
    assert "book1" not in borrower.borrowed_resource_ids
