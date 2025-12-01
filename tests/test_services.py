import pytest
import os
from library_system.services.library_manager import LibraryManager
from library_system.models.book import Book
from library_system.models.ebook import EBook

@pytest.fixture
def test_db():
    file_path = "tests/test_library.json"
    if os.path.exists(file_path):
        os.remove(file_path)
    yield file_path
    if os.path.exists(file_path):
        os.remove(file_path)

def test_add_resource(test_db):
    manager = LibraryManager(test_db)
    book = Book("1", "Test Book", "Author", "123", 100)
    manager.add_resource(book)
    
    assert len(manager.resources) == 1
    assert manager.get_resource("1") == book

def test_persistence(test_db):
    # Save
    manager1 = LibraryManager(test_db)
    ebook = EBook("2", "E-Book", "Author", "456", 200, 1.5, "PDF")
    manager1.add_resource(ebook)
    
    # Load
    manager2 = LibraryManager(test_db)
    loaded_ebook = manager2.get_resource("2")
    
    assert isinstance(loaded_ebook, EBook)
    assert loaded_ebook.title == "E-Book"
    assert loaded_ebook.file_format == "PDF"

def test_search(test_db):
    manager = LibraryManager(test_db)
    manager.add_resource(Book("1", "Python 101", "Guido", "111", 50))
    manager.add_resource(Book("2", "Java 101", "Gosling", "222", 60))
    
    results = manager.search_resources("Python")
    assert len(results) == 1
    assert results[0].title == "Python 101"

def test_remove_resource(test_db):
    manager = LibraryManager(test_db)
    manager.add_resource(Book("1", "Delete Me", "Author", "000", 10))
    manager.remove_resource("1")
    assert len(manager.resources) == 0
