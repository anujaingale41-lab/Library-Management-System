import json
import os

class FileManager:
    def load_json(self, filepath):
        if not os.path.exists(filepath):
            return []
        with open(filepath, 'r') as f:
            return json.load(f)

    def save_json(self, filepath, data):
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
