import json
import sys
filename = "storage.json"

sys.stderr = open("error_log.txt", 'w')

def load_json_file():
    """
    Safely attempts to load data from a JSON file.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.", file=sys.stderr)
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the file '{filename}'.", file=sys.stderr)
    
    
