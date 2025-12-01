from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class LibraryResource(ABC):
    """Abstract base class for all library resources."""
    
    resource_id: str
    title: str
    author: str
    
    @abstractmethod
    def get_details(self) -> str:
        """Return a formatted string of resource details."""
        pass
    
    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
