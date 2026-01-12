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

            elif validation_type == "email":
                # Simple, human-friendly check: must have '@' and '.'
                if "@" in user_input and "." in user_input:
                    # Basic check to ensure characters exist around the symbols
                    if user_input.find("@") < user_input.rfind("."):
                        return user_input.lower() # Standardize email to lowercase
                print("Error: Invalid email format. Must contain '@' and a domain (e.g., '.com').")
        
            else:
                return user_input # Default for general text
            
    
    full_name = get_valid_input("Enter your name: ", "name")
    email = get_valid_input("Enter your email: ", "email")
    
    data["candidate"] = {"fullname": full_name,
                         "email": email}
    
    storage.save_json_file(data)
    print(f"Welcome {data['candidate']['fullname']}. Your onboarding is done.")
