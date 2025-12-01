# Library Inventory Application

![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-13%20passing-brightgreen)

A Python-based Library Inventory Application to manage books, authors, and borrowers. This project demonstrates Object-Oriented Programming (OOP) principles including inheritance, polymorphism, and abstraction.

## 🎯 Features

- **Resource Management**: 
  - **Books**: Track physical books with ISBN and page counts.
  - **E-Books**: Manage digital formats (PDF/EPUB) and file sizes.
  - **Audiobooks**: Track duration and narrators.
- **Inventory Control**:
  - Add, remove, and list resources.
  - Case-insensitive search by title or author.
- **Borrowing System**: 
  - Track borrowers and their loaned items.
- **Data Persistence**: 
  - Automatic JSON-based storage (`data/library.json`).
  - Data persists between sessions.
- **Interactive CLI**: 
  - User-friendly menu system.
  - Robust input validation.

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/franakol/library-inventory-app.git
   cd library-inventory-app
   ```

2. **Set up Virtual Environment**
   ```bash
   # Create virtual environment
   python3 -m venv .venv
   
   # Activate it
   source .venv/bin/activate  # macOS/Linux
   # .venv\Scripts\activate   # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install pytest black flake8 mypy
   ```

### Running the Application

To start the interactive Command-Line Interface (CLI):

```bash
python -m library_system.main
```

## 📖 Usage Guide

### Main Menu
When you launch the app, you'll see the main menu:

```text
=== Library Inventory System ===
1. Add Resource
2. List All Resources
3. Search Resources
4. Remove Resource
5. Exit
```

### Adding Resources
Select option **1** to add a new item. You will be prompted to choose the type:

1. **Physical Book**: Requires ISBN and Page Count.
2. **E-Book**: Requires File Size (MB) and Format (e.g., PDF).
3. **Audiobook**: Requires Duration (mins) and Narrator.

**Example Input:**
```text
Resource ID: 101
Title: The Great Gatsby
Author: F. Scott Fitzgerald
ISBN: 978-0743273565
Page Count: 180
```

### Searching
Select option **3** to search. You can enter a partial title or author name.
*   Query: "gatsby" -> Finds "The Great Gatsby"
*   Query: "fitzgerald" -> Finds "The Great Gatsby"

## 🧪 Testing

The project includes a comprehensive test suite using `pytest`.

### Running Tests
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v
```

### Test Structure
- `tests/test_models.py`: Verifies OOP classes (Book, EBook, Author).
- `tests/test_services.py`: Verifies LibraryManager and JSON persistence.
- `tests/test_cli.py`: Verifies CLI menu flows and user interaction.

## 📁 Project Structure

```
library-inventory-app/
├── library_system/
│   ├── models/          # Domain Entities
│   │   ├── resource.py  # Abstract Base Class
│   │   ├── book.py      # Concrete Class
│   │   ├── ebook.py     # Inherits from Book
│   │   └── ...
│   ├── services/        # Business Logic
│   │   └── library_manager.py
│   ├── ui/              # User Interface
│   │   └── cli.py
│   ├── utils/           # Utilities
│   │   └── storage.py   # JSON Persistence
│   └── main.py          # Entry Point
├── tests/               # Unit Tests
├── data/                # Data Storage (Auto-generated)
└── docs/                # Documentation
```

## 📝 License

This project is created for educational purposes.
