import json
from pathlib import Path
from typing import List, Dict, Any

class Storage:
    """Handles JSON file persistence for library data."""
    
    @staticmethod
    def save_data(file_path: str, data: List[Dict[str, Any]]) -> None:
        """Save a list of dictionaries to a JSON file."""
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            
    @staticmethod
    def load_data(file_path: str) -> List[Dict[str, Any]]:
        """Load a list of dictionaries from a JSON file."""
        path = Path(file_path)
        if not path.exists():
            return []
            
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
