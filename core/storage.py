import json
import logging
filename = "storage.json"

# Configuring logging to write to a file
logging.basicConfig(
    filename='app.log', 
    level=logging.ERROR, # logging for ERROR (40)
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
        logging.error("The file 'storage.json' was not found. Creating a new default structure.")
        
        # if file not exists creating a default empty structure
        default_structure = {
            "candidate": None,
            "skills": [],
            "applications":[] 
        }
        
        with open(filename, 'w') as file:
            json.dump(default_structure, file, indent=4)
            
        return default_structure
    
    except json.JSONDecodeError as e:
        logging.error(f"Failed to decode JSON: {e}")
        

def save_json_file(data):
    """
    Accepts the full data object and overwrites the storage file safely.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        
    except (OSError, IOError) as e:
        # Logs physical disk errors (e.g., permission denied, disk full)
        logging.error(f"Reliability Error: Could not write to {filename}. Details: {e}")
        
    except Exception as e:
        logging.error(f"Unexpected Write Failure: {e}")
        
    
    
    
