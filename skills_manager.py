import storage

def manage_skills(data):
    """Entry point for skill-related actions."""
    while True:
        print("\n--- MANAGE SKILLS ---")
        list_skills(data)
        print("\n1. Add Skill")
        print("2. Back to Dashboard")
        
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_skill(data)
        elif choice == "2":
            break
        else:
            print("Invalid choice.")



def list_skills(data):
    """Displays current skills from the data object."""
    skills = data.get("skills", [])
    if not skills:
        print("Your skills list is currently empty.")
    else:
        print("Your Skills:")
        for idx, skill in enumerate(skills, 1):
            print(f"{idx}. {skill}")


def add_skill(data):
    """Prompts, validates, and adds a unique skill."""
    new_skill = input("Enter the skill to add: ").strip().lower()
    
    # empty input check
    if not new_skill:
        print("Input can not be empty")
        return

    # Validation Rules
    # If "skills" is missing or None, we take it as an empty list []
    if "skills" not in data or not isinstance(data["skills"], list):
        data["skills"] = []

    if new_skill in data["skills"]:
        print(f"Error: '{new_skill}' is already in your skills list.")
        return

    # Success Path: Update and Save
    data["skills"].append(new_skill)
    storage.save_json_file(data)
    print(f"Success: '{new_skill}' added and saved.")