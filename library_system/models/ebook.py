from dataclasses import dataclass
from .book import Book

@dataclass
class EBook(Book):
    """Concrete class representing an electronic book."""
    
    file_size_mb: float
    file_format: str  # e.g., 'PDF', 'EPUB'
    
    def get_details(self) -> str:
        base_details = super().get_details()
        return (
            f"{base_details}\n"
            f"Format: {self.file_format}\n"
            f"Size: {self.file_size_mb} MB"
        )
