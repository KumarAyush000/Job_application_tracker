import core.storage as storage

def onboard_candidate(data):
    
    print("--- Onboarding: New Candidate ---")
    
    
    def get_valid_input(prompt, validation_type="text"):
        while True:
            # Prompt and immediately strip whitespace
            user_input = input(f"{prompt}: ").strip()

            # Rule 1: Reject empty input for both types
            if not user_input:
                print("Error: Input cannot be empty. Please try again.")
                continue

            if validation_type == "name":
                # Simple check: Is it just letters and spaces?
                if all(char.isalpha() or char.isspace() for char in user_input):
                    return user_input
                print("Error: Please enter a valid name (letters only).")

        
            else:
                return user_input # Default for general text
            
    
    full_name = get_valid_input("Enter your name ", "name")
    
    data["candidate"] = {"fullname": full_name}
    
    storage.save_json_file(data)
    print(f"Welcome {data['candidate']['fullname']}. Your onboarding is done.")


def login_user(data):
    users = data.get("users", {})

    if not users:
        print("No users found. Please create a user first.")
        return None

    user_id = input("Enter your User ID (e.g. U001): ").strip()

    if not user_id:
        print("User ID cannot be empty.")
        return None

    if user_id not in users:
        print("Invalid User ID.")
        return None

    print(f"Login successful. Welcome, {users[user_id]['name']}!")
    return user_id
