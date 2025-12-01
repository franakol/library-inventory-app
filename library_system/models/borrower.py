from dataclasses import dataclass, field
from typing import List

@dataclass
class Borrower:
    """Represents a library member who can borrow books."""
    
    name: str
    email: str
    borrowed_resource_ids: List[str] = field(default_factory=list)
    
    def borrow_resource(self, resource_id: str) -> None:
        if resource_id not in self.borrowed_resource_ids:
            self.borrowed_resource_ids.append(resource_id)
            
    def return_resource(self, resource_id: str) -> None:
        if resource_id in self.borrowed_resource_ids:
            self.borrowed_resource_ids.remove(resource_id)
            
    def __str__(self) -> str:
        return f"{self.name} ({self.email})"
