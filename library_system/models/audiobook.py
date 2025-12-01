from dataclasses import dataclass
from .book import Book

@dataclass
class Audiobook(Book):
    """Concrete class representing an audiobook."""
    
    duration_minutes: int
    narrator: str
    
    def get_details(self) -> str:
        base_details = super().get_details()
        return (
            f"{base_details}\n"
            f"Narrator: {self.narrator}\n"
            f"Duration: {self.duration_minutes} min"
        )
