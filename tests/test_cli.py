import pytest
from unittest.mock import patch, MagicMock
from library_system.ui.cli import CLI

@pytest.fixture
def mock_manager():
    with patch('library_system.ui.cli.LibraryManager') as MockManager:
        yield MockManager.return_value

def test_cli_initialization(mock_manager):
    cli = CLI()
    assert cli.manager == mock_manager

def test_add_book_flow(mock_manager):
    cli = CLI()
    # Simulate inputs: Choice 1 (Add), Choice 1 (Book), ID, Title, Author, ISBN, Pages
    inputs = ['1', '1', 'B1', 'Test Book', 'Author', '123', '100', '5']
    
    with patch('builtins.input', side_effect=inputs):
        with pytest.raises(SystemExit):
            cli.start()
            
    mock_manager.add_resource.assert_called_once()

def test_search_flow(mock_manager):
    cli = CLI()
    inputs = ['3', 'Python', '5']
    
    with patch('builtins.input', side_effect=inputs):
        with pytest.raises(SystemExit):
            cli.start()
            
    mock_manager.search_resources.assert_called_with('Python')

def test_remove_flow(mock_manager):
    cli = CLI()
    mock_manager.get_resource.return_value = True
    inputs = ['4', 'B1', '5']
    
    with patch('builtins.input', side_effect=inputs):
        with pytest.raises(SystemExit):
            cli.start()
            
    mock_manager.remove_resource.assert_called_with('B1')
