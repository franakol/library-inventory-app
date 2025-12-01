from typing import List, Optional, Dict, Any
from library_system.models.resource import LibraryResource
from library_system.models.book import Book
from library_system.models.ebook import EBook
from library_system.models.audiobook import Audiobook
from library_system.utils.storage import Storage

class LibraryManager:
    """Manages library inventory and operations."""
    
    def __init__(self, storage_file: str = "data/library.json"):
        self.storage_file = storage_file
        self.resources: List[LibraryResource] = []
        self._load_resources()
        
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
