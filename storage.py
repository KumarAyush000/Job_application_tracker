import json
import logging
filename = "storage.json"

# Configuring logging to write to a file
logging.basicConfig(
    filename='app.log', 
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_json_file():
    """
    Safely attempts to load data from a JSON file.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            
        return data
    except FileNotFoundError:
        logging.error("The file 'storage.json' was not found.")
    except json.JSONDecodeError as e:
        logging.error(f"Failed to decode JSON: {e}")
        
    
