import sys
from typing import Optional
from library_system.services.library_manager import LibraryManager
from library_system.models.book import Book
from library_system.models.ebook import EBook
from library_system.models.audiobook import Audiobook

class CLI:
    """Command-line interface for the Library Inventory Application."""
    
    def __init__(self):
        self.manager = LibraryManager()
        
    def start(self):
        """Start the CLI application."""
        while True:
            self._display_menu()
            choice = input("\nEnter your choice (1-6): ")
            
            if choice == '1':
                self._add_resource_menu()
            elif choice == '2':
                self._list_resources()
            elif choice == '3':
                self._search_resources()
            elif choice == '4':
                self._remove_resource()
            elif choice == '5':
                self._view_reports()
            elif choice == '6':
                print("\nGoodbye!")
                sys.exit(0)
            else:
                print("\nInvalid choice. Please try again.")
                
    def _display_menu(self):
        print("\n=== Library Inventory System ===")
        print("1. Add Resource")
        print("2. List All Resources")
        print("3. Search Resources")
        print("4. Remove Resource")
        print("5. View Reports")
        print("6. Exit")
        
    def _add_resource_menu(self):
        print("\nSelect Resource Type:")
        print("1. Physical Book")
        print("2. E-Book")
        print("3. Audiobook")
        
        type_choice = input("Choice (1-3): ")
        
        try:
            if type_choice == '1':
                self._add_book()
            elif type_choice == '2':
                self._add_ebook()
            elif type_choice == '3':
                self._add_audiobook()
            else:
                print("Invalid resource type.")
        except ValueError as e:
            print(f"\nError: {e}")
            
    def _get_common_details(self):
        resource_id = input("Resource ID: ")
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        page_count = int(input("Page Count: "))
        return resource_id, title, author, isbn, page_count
        
    def _add_book(self):
        details = self._get_common_details()
        book = Book(*details)
        self.manager.add_resource(book)
        print("\nBook added successfully!")
        
    def _add_ebook(self):
        details = self._get_common_details()
        file_size = float(input("File Size (MB): "))
        file_format = input("Format (PDF/EPUB): ")
        ebook = EBook(*details, file_size_mb=file_size, file_format=file_format)
        self.manager.add_resource(ebook)
        print("\nE-Book added successfully!")
        
    def _add_audiobook(self):
        details = self._get_common_details()
        duration = int(input("Duration (minutes): "))
        narrator = input("Narrator: ")
        audiobook = Audiobook(*details, duration_minutes=duration, narrator=narrator)
        self.manager.add_resource(audiobook)
        print("\nAudiobook added successfully!")
        
    def _list_resources(self):
        resources = self.manager.get_all_resources()
        if not resources:
            print("\nNo resources found.")
            return
            
        print(f"\nTotal Resources: {len(resources)}")
        for r in resources:
            print("-" * 40)
            print(r.get_details())
            
    def _search_resources(self):
        query = input("\nEnter search query (title or author): ")
        results = self.manager.search_resources(query)
        
        if not results:
            print("\nNo matches found.")
            return
            
        print(f"\nFound {len(results)} matches:")
        for r in results:
            print("-" * 40)
            print(r.get_details())
            
    def _remove_resource(self):
        resource_id = input("\nEnter Resource ID to remove: ")
        if self.manager.get_resource(resource_id):
            self.manager.remove_resource(resource_id)
            print("\nResource removed successfully.")
        else:
            print("\nResource not found.")
    
    def _view_reports(self):
        """Display library reports using list comprehensions."""
        print("\n=== Library Reports ===\n")
        
        # Inventory Report
        print("--- Inventory Summary ---")
        inventory = self.manager.generate_inventory_report()
        print(f"Total Physical Books: {inventory['total_books']}")
        print(f"Total E-Books: {inventory['total_ebooks']}")
        print(f"Total Audiobooks: {inventory['total_audiobooks']}")
        print(f"Total Resources: {inventory['total_resources']}")
        
        # Borrowing Report
        print("\n--- Borrowing Statistics ---")
        borrowing = self.manager.generate_borrowing_report()
        print(f"Total Borrowers: {borrowing['total_borrowers']}")
        print(f"Active Borrowers: {borrowing['active_borrowers']}")
        print(f"Total Borrowed Items: {borrowing['total_borrowed_items']}")
        print(f"Available Items: {borrowing['available_items']}")
        
        # Currently Borrowed Resources
        borrowed_list = self.manager.get_borrowed_resources_list()
        if borrowed_list:
            print("\n--- Currently Borrowed Resources ---")
            for item in borrowed_list:
                print(f"  - {item['resource_title']} (ID: {item['resource_id']}) borrowed by {item['borrower']}")
        else:
            print("\n--- No resources currently borrowed ---")
