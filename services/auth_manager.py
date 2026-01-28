"""
module for authantication of the user
"""
import core.storage as storage
from datetime import datetime


def create_user(data):
    """
    Creates a new user and saves it to storage.
    """
    username = input("Enter username: ").strip().lower()

    if not username:
        print("Username cannot be empty.")
        return None

    # Ensure users container exists
    if "users" not in data or not isinstance(data["users"], dict):
        data["users"] = {}

    user_id = _generate_user_id(data)

    data["users"][user_id] = {
        "username": username,
        "skills": [],
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }

    storage.save_json_file(data)
    print(f"User created successfully. User ID: {user_id}")

    return user_id


def _generate_user_id(data):
    """
    Generates unique user IDs like U001, U002...
    """
    existing_ids = data.get("users", {}).keys()
    numbers = [
        int(uid[1:]) for uid in existing_ids if uid.startswith("U")
    ]

    next_number = max(numbers) + 1 if numbers else 1
    return f"U{next_number:03d}"


def login_user(data):
    user_id = input("Enter your User ID: ").strip()

    if "users" not in data or user_id not in data["users"]:
        print("Invalid User ID.")
        return None

    print("Login successful.")
    return user_id


def get_user(data, user_id):
    if "users" not in data:
        return None
    
    user = data["users"].get(user_id)

    if not isinstance(user, dict):
        return None
    
    if "skills" not in user or not isinstance(user["skills"], list):
        user["skills"] = []

    return user