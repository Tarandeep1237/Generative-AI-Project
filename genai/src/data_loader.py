import json
from typing import List, Dict

def load_questions(file_path: str) -> List[Dict]:
    """Loads questions from a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return []
