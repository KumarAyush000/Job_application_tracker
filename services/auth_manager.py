"""
module for authantication of the user
"""

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