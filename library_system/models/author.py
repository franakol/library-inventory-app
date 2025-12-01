from dataclasses import dataclass, field
from typing import List

@dataclass
class Author:
    """Represents an author with a collection of books."""
    
    name: str
    biography: str = ""
    book_ids: List[str] = field(default_factory=list)
    
    def add_book(self, book_id: str) -> None:
        if book_id not in self.book_ids:
            self.book_ids.append(book_id)
            
    def __str__(self) -> str:
        return self.name
