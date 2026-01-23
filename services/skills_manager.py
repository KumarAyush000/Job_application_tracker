import core.storage as storage
import validators.validators as validators

def manage_skills(data, current_user_id):
    """
    HARD GUARD: Prevent access without login
    """
    if current_user_id is None:
        print("Access denied. Please log in to manage skills.")
        return
    
    if "users" not in data or current_user_id not in data["users"]:
        print("Invalid user session.")
        return
    
    user = data["users"][current_user_id]

    while True:
        print("\n--- MANAGE SKILLS ---")
        list_skills(user)
        print("\n1. Add Skill")
        print("2. Edit Skill")
        print("3. Delete Skill")
        print("4. Back to Dashboard")
        
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_skill(user, data)
        elif choice == "2":
            edit_skill(user, data)
        elif choice == "3":
            delete_skill(user, data)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def list_skills(user):
    """Displays current skills from the data object."""
    skills = user.get("skills", [])
    if validators.empty_list_checker(skills):
        print("Your skills list is currently empty.")
    else:
        print("Your Skills:")
        for idx, skill in enumerate(skills, 1):
            print(f"{idx}. {skill}")


def add_skill(user, data):
    """Prompts, validates, and adds a unique skill."""
    new_skill = input("Enter the skill to add: ").strip().lower()

    # empty input check
    if validators.empty_input_checker(new_skill):
        print("Input can not be empty")
        return

    # Validation Rules
    # If "skills" is missing or None, we take it as an empty list []
    if "skills" not in user or not isinstance(user["skills"], list):
        user["skills"] = []

    # duplicacy checking
    if new_skill in user["skills"]:
        print(f"Error: '{new_skill}' is already in your skills list.")
        return

    # Success Path: Update and Save
    user["skills"].append(new_skill)
    storage.save_json_file(data)
    print(f"Success: '{new_skill}' added and saved.")


def edit_skill(user, data):
    """Prompts, validates, and edits an existing skill."""
    skills = user.get("skills", [])
    
    if not isinstance(skills, list) or validators.empty_list_checker(skills):
        print("Your skills list is currently empty or invalid. Nothing to edit.")
        return
    
    skill_to_edit = input("Enter the index number of the skill you want to edit: ").strip()
    
    # empty input check
    if validators.empty_input_checker(skill_to_edit):
        print("Index can not be empty.")
        return
    
    index = validators.get_valid_index(skill_to_edit, skills)
    if index is None:
        print("Invalid Index.")
        return

    new_skill_name = input("Enter the new skill name: ").strip().lower()
    if validators.empty_input_checker(new_skill_name):
        print("Skill name can not be empty.")
        return         

    # Duplicacy prevention
    if new_skill_name in skills and skills[index] != new_skill_name:
        print("Skill already exists.")
        return          

    # Editing skill and saving it to the system
    old_skill = skills[index]
    skills[index] = new_skill_name

    storage.save_json_file(data)
    print(f"Success: '{old_skill}' updated to '{new_skill_name}' and saved.")   


def delete_skill(user, data):
    """Prompts, validates, and deletes an existing skill."""
    skills = user.get("skills", [])
    
    if not isinstance(skills, list) or validators.empty_list_checker(skills):
        print("Your skills list is currently empty or invalid. Nothing to delete.")
        return
    
    skill_to_delete = input("Enter the index number of the skill you want to delete: ").strip()
    
    # empty input check
    if validators.empty_input_checker(skill_to_delete):
        print("Index can not be empty.")
        return
    
    index = validators.get_valid_index(skill_to_delete, skills)
    if index is None:
        print("Invalid index.")
        return

    # confirmation
    skill_name = skills[index]
    confirmation = input(
        f"Are you sure you want to delete this skill: {skill_name}. "
        "Type: ('Y' for yes OR 'N' for no): "
    ).strip().lower()

    if confirmation == 'n':
        print("Exiting the deletion process...")
        return
    elif confirmation == 'y':
        skills.pop(index)
        storage.save_json_file(data)
        print(f"Success: {skill_name} has been deleted.")
    else:
        print("Invalid input for the confirmation.")
