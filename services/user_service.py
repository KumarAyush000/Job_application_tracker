

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