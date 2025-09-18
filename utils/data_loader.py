import json
import os

class DataLoader:
    @staticmethod
    def load_json(file_name: str):
        file_path = os.path.join(os.path.dirname(__file__), "..", "data", file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
