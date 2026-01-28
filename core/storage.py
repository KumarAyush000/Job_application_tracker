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

        _ensure_schema_v2(data)
        return data

    except FileNotFoundError:
        logging.error("The file 'storage.json' was not found. Creating a new default structure.")

        default_structure = _default_structure()

        with open(filename, 'w') as file:
            json.dump(default_structure, file, indent=4)

        return default_structure

    except json.JSONDecodeError as e:
        logging.error(f"Failed to decode JSON: {e}")

        # recover with safe structure
        default_structure = _default_structure()
        save_json_file(default_structure)
        return default_structure


def save_json_file(data):
    """
    Accepts the full data object and overwrites the storage file safely.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    except (OSError, IOError) as e:
        logging.error(f"Reliability Error: Could not write to {filename}. Details: {e}")

    except Exception as e:
        logging.error(f"Unexpected Write Failure: {e}")


# -------------------- INTERNAL HELPERS --------------------

def _default_structure():
    """
    Default Schema v2 structure.
    Backward compatible.
    """
    return {
        "candidate": None,
        "users": {},
        "roles": {},
        "applications": {}
    }


def _ensure_schema_v2(data):
    """
    Ensures required keys exist for Schema v2.
    Prevents crashes when upgrading old data.
    """
    if "candidate" not in data:
        data["candidate"] = None

    # old schema compatibility cleanup
    if "skills" in data:
        del data["skills"]

    if "applications" not in data:
        data["applications"] = {}

    if "users" not in data:
        data["users"] = {}

    if "roles" not in data:
        data["roles"] = {}
