from dataclasses import dataclass
from .resource import LibraryResource

@dataclass
class Book(LibraryResource):
    """Concrete class representing a physical book."""
    
    isbn: str
    page_count: int
    
    def get_details(self) -> str:
        return (
            f"Book: {self.title}\n"
            f"Author: {self.author}\n"
            f"ISBN: {self.isbn}\n"
            f"Pages: {self.page_count}"
        )
