from typing import List, Optional, Dict, Any
from library_system.models.resource import LibraryResource
from library_system.models.book import Book
from library_system.models.ebook import EBook
from library_system.models.audiobook import Audiobook
from library_system.models.borrower import Borrower
from library_system.utils.storage import Storage

class LibraryManager:
    """Manages library inventory and operations."""
    
    def __init__(self, storage_file: str = "data/library.json", borrower_file: str = "data/borrowers.json"):
        self.storage_file = storage_file
        self.borrower_file = borrower_file
        self.resources: List[LibraryResource] = []
        self.borrowers: List[Borrower] = []
        self._load_resources()
        self._load_borrowers()
        
    def add_resource(self, resource: LibraryResource) -> None:
        """Add a new resource to the library."""
        if any(r.resource_id == resource.resource_id for r in self.resources):
            raise ValueError(f"Resource with ID {resource.resource_id} already exists.")
        
        self.resources.append(resource)
        self._save_resources()
        
    def remove_resource(self, resource_id: str) -> None:
        """Remove a resource by ID."""
        resource = self.get_resource(resource_id)
        if resource:
            self.resources.remove(resource)
            self._save_resources()
            
    def get_resource(self, resource_id: str) -> Optional[LibraryResource]:
        """Find a resource by ID."""
        return next((r for r in self.resources if r.resource_id == resource_id), None)
        
    def search_resources(self, query: str) -> List[LibraryResource]:
        """Search resources by title or author (case-insensitive)."""
        query = query.lower()
        return [
            r for r in self.resources 
            if query in r.title.lower() or query in r.author.lower()
        ]
        
    def get_all_resources(self) -> List[LibraryResource]:
        """Return all resources."""
        return self.resources
    
    # Borrower Management
    
    def add_borrower(self, borrower: Borrower) -> None:
        """Add a new borrower."""
        if any(b.email == borrower.email for b in self.borrowers):
            raise ValueError(f"Borrower with email {borrower.email} already exists.")
        self.borrowers.append(borrower)
        self._save_borrowers()
    
    def get_borrower(self, email: str) -> Optional[Borrower]:
        """Find a borrower by email."""
        return next((b for b in self.borrowers if b.email == email), None)
    
    def get_all_borrowers(self) -> List[Borrower]:
        """Return all borrowers."""
        return self.borrowers
    
    # Borrowing Operations
    
    def borrow_resource(self, borrower_email: str, resource_id: str) -> None:
        """Borrow a resource."""
        borrower = self.get_borrower(borrower_email)
        if not borrower:
            raise ValueError(f"Borrower with email {borrower_email} not found.")
        
        resource = self.get_resource(resource_id)
        if not resource:
            raise ValueError(f"Resource with ID {resource_id} not found.")
        
        # Check if already borrowed using list comprehension
        if any(resource_id in b.borrowed_resource_ids for b in self.borrowers):
            raise ValueError(f"Resource {resource_id} is already borrowed.")
        
        borrower.borrow_resource(resource_id)
        self._save_borrowers()
    
    def return_resource(self, borrower_email: str, resource_id: str) -> None:
        """Return a borrowed resource."""
        borrower = self.get_borrower(borrower_email)
        if not borrower:
            raise ValueError(f"Borrower with email {borrower_email} not found.")
        
        if resource_id not in borrower.borrowed_resource_ids:
            raise ValueError(f"Borrower {borrower_email} hasn't borrowed resource {resource_id}.")
        
        borrower.return_resource(resource_id)
        self._save_borrowers()
    
    # Library Reports using List Comprehensions
    
    def generate_inventory_report(self) -> Dict[str, int]:
        """Generate inventory summary using list comprehensions."""
        return {
            "total_books": len([r for r in self.resources if isinstance(r, Book) and not isinstance(r, (EBook, Audiobook))]),
            "total_ebooks": len([r for r in self.resources if isinstance(r, EBook)]),
            "total_audiobooks": len([r for r in self.resources if isinstance(r, Audiobook)]),
            "total_resources": len(self.resources)
        }
    
    def generate_borrowing_report(self) -> Dict[str, Any]:
        """Generate borrowing statistics using list comprehensions."""
        all_borrowed_ids = [rid for b in self.borrowers for rid in b.borrowed_resource_ids]
        return {
            "total_borrowers": len(self.borrowers),
            "active_borrowers": len([b for b in self.borrowers if b.borrowed_resource_ids]),
            "total_borrowed_items": len(all_borrowed_ids),
            "available_items": len(self.resources) - len(set(all_borrowed_ids))
        }
    
    def get_borrowed_resources_list(self) -> List[Dict[str, str]]:
        """Get list of all borrowed resources using list comprehensions."""
        return [
            {
                "borrower": b.name, 
                "resource_id": rid, 
                "resource_title": self.get_resource(rid).title if self.get_resource(rid) else "Unknown"
            }
            for b in self.borrowers
            for rid in b.borrowed_resource_ids
        ]
        
    def _save_resources(self) -> None:
        """Persist resources to storage."""
        data = [self._resource_to_dict(r) for r in self.resources]
        Storage.save_data(self.storage_file, data)
        
    def _load_resources(self) -> None:
        """Load resources from storage."""
        data = Storage.load_data(self.storage_file)
        self.resources = [self._dict_to_resource(d) for d in data]
        
    def _resource_to_dict(self, resource: LibraryResource) -> Dict[str, Any]:
        """Convert resource object to dictionary."""
        data = {
            "type": resource.__class__.__name__,
            "resource_id": resource.resource_id,
            "title": resource.title,
            "author": resource.author,
            "isbn": resource.isbn,
            "page_count": resource.page_count
        }
        
        if isinstance(resource, EBook):
            data.update({
                "file_size_mb": resource.file_size_mb,
                "file_format": resource.file_format
            })
        elif isinstance(resource, Audiobook):
            data.update({
                "duration_minutes": resource.duration_minutes,
                "narrator": resource.narrator
            })
            
        return data
        
    def _dict_to_resource(self, data: Dict[str, Any]) -> LibraryResource:
        """Convert dictionary to resource object."""
        res_type = data.pop("type")
        
        if res_type == "EBook":
            return EBook(**data)
        elif res_type == "Audiobook":
            return Audiobook(**data)
        elif res_type == "Book":
            return Book(**data)
        else:
            raise ValueError(f"Unknown resource type: {res_type}")
    
    def _save_borrowers(self) -> None:
        """Persist borrowers to storage."""
        data = [self._borrower_to_dict(b) for b in self.borrowers]
        Storage.save_data(self.borrower_file, data)
    
    def _load_borrowers(self) -> None:
        """Load borrowers from storage."""
        data = Storage.load_data(self.borrower_file)
        self.borrowers = [self._dict_to_borrower(d) for d in data]
    
    def _borrower_to_dict(self, borrower: Borrower) -> Dict[str, Any]:
        """Convert borrower object to dictionary."""
        return {
            "name": borrower.name,
            "email": borrower.email,
            "borrowed_resource_ids": borrower.borrowed_resource_ids
        }
    
    def _dict_to_borrower(self, data: Dict[str, Any]) -> Borrower:
        """Convert dictionary to borrower object."""
        return Borrower(**data)
