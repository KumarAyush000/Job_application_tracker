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
