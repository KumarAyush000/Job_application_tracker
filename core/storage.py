import json
import logging

filename = "storage.json"

# Configuring logging to write to a file
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_json_file():
    """
    Safely attempts to load data from a JSON file.
    Applies Schema v2 guarantees.
    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        # ensures schema compatibility
        schema_updated = _ensure_schema_v2(data)

        # persists migration if needed
        if schema_updated:
            save_json_file(data)

        return data

    except FileNotFoundError:
        logging.error("storage.json not found. Initializing Schema v2.")

        default_structure = _default_structure()
        save_json_file(default_structure)
        return default_structure

    except json.JSONDecodeError as e:
        logging.error(f"Failed to decode JSON: {e}")

        # recover safely
        default_structure = _default_structure()
        save_json_file(default_structure)
        return default_structure


def save_json_file(data):
    """
    Accepts the full data object and overwrites the storage file safely.
    """
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    except (OSError, IOError) as e:
        logging.error(f"Reliability Error: Could not write to {filename}. Details: {e}")

    except Exception as e:
        logging.error(f"Unexpected Write Failure: {e}")


# -------------------- INTERNAL HELPERS --------------------

def _default_structure():
    """
    Default Schema v2 structure.
    """
    return {
        "candidate": None,
        "users": {},
        "roles": {},
        "applications": {},
        "meta": {
            "schema_version": "2.0"
        }
    }


def _ensure_schema_v2(data):
    """
    Ensures required keys exist for Schema v2.
    Returns True if mutation occurred.
    """
    updated = False

    if "candidate" not in data:
        data["candidate"] = None
        updated = True

    if "users" not in data or not isinstance(data["users"], dict):
        data["users"] = {}
        updated = True

    if "roles" not in data or not isinstance(data["roles"], dict):
        data["roles"] = {}
        updated = True

    if "applications" not in data or not isinstance(data["applications"], dict):
        data["applications"] = {}
        updated = True

    if "meta" not in data:
        data["meta"] = {"schema_version": "2.0"}
        updated = True

    return updated
