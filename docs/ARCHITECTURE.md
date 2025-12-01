# System Architecture - Library Inventory Application

## Overview

The Library Inventory Application follows a **layered architecture** pattern with clear separation of concerns. The system is designed using Object-Oriented Programming principles to demonstrate inheritance, polymorphism, and abstraction.

## Architecture Layers

```
┌─────────────────────────────────────────┐
│         Presentation Layer              │
│              (UI/CLI)                   │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│         Service Layer                   │
│       (Business Logic)                  │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│         Domain Layer                    │
│          (Models)                       │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│         Data Layer                      │
│      (File Persistence)                 │
└─────────────────────────────────────────┘
```

## Layer Details

### 1. Domain Layer (`models/`)

**Purpose**: Core business entities and rules

**Components**:
- `LibraryResource` (Abstract Base Class)
  - Defines common attributes: `resource_id`, `title`, `author`
  - Enforces contract via `@abstractmethod`
  
- `Book` (Concrete Class)
  - Attributes: `isbn`, `page_count`
  
- `EBook` (Concrete Class)
  - Inherits from `Book`
  - Attributes: `file_size`, `format`
  
- `Audiobook` (Concrete Class)
  - Inherits from `Book`
  - Attributes: `duration`, `narrator`

### 2. Service Layer (`services/`)

**Purpose**: Business operations and orchestration

**Components**:
- `LibraryManager`
  - **Inventory Control**: Add, remove, search resources
  - **Borrowing**: Check-out and return logic
  - **Persistence**: Save/load state

### 3. Data Layer (`utils/`)

**Purpose**: Data storage and retrieval

**Implementation**:
- JSON file format
- `Storage` utility class for serialization

### 4. Presentation Layer (`ui/`)

**Purpose**: User interaction

**Components**:
- `CLI`: Interactive menu system
