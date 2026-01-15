from validators import empty_input_checker
from services import storage

def generate_user_id(users):
    """
    Generates a new unique user ID in the format U001, U002, ...
    """
    if not users:
        return "U001"

    # Extract numeric part of IDs and find max
    last_id = max(users.keys())
    last_number = int(last_id[1:])
    new_number = last_number + 1

    return f"U{new_number:03d}"


def create_user(data):
    """
    Creates a new user with a unique ID and empty skills list.
    """
    users = data.get("users")

    if not isinstance(users, list):
        print("User data is corrupted.")
        return

    name = input("Enter your name: ").strip()

    if empty_input_checker(name):
        print("Name cannot be empty.")
        return

    user_id = generate_user_id(users)

    user = {
        "user_id": user_id,
        "name": name,
        "skills": []
    }

    users.append(user)
    storage.save_json_file(data)

    print(f"User created successfully!")
    print(f"Your User ID is: {user_id}")

