import core.storage as storage
import validators.validators as validators

def manage_skills(data):
    """Entry point for skill-related actions."""
    while True:
        print("\n--- MANAGE SKILLS ---")
        list_skills(data)
        print("\n1. Add Skill")
        print("2. Edit Skill")
        print("3. Delete Skill")
        print("4. Back to Dashboard")
        
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_skill(data)
        elif choice == "2":
            edit_skill(data)
        elif choice == "3":
            delete_skill(data)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")



def list_skills(data):
    """Displays current skills from the data object."""
    skills = data.get("skills", [])
    if validators.empty_list_checker(skills):
        print("Your skills list is currently empty.")
    else:
        print("Your Skills:")
        for idx, skill in enumerate(skills, 1):
            print(f"{idx}. {skill}")


def add_skill(data):
    """Prompts, validates, and adds a unique skill."""
    new_skill = input("Enter the skill to add: ").strip().lower()
    # empty input check
    if validators.empty_input_checker(new_skill):
        print("Input can not be empty")
        return

    # Validation Rules
    # If "skills" is missing or None, we take it as an empty list []
    if "skills" not in data or not isinstance(data["skills"], list):
        data["skills"] = []

    # duplicacy checking
    if new_skill in data["skills"]:
        print(f"Error: '{new_skill}' is already in your skills list.")
        return

    # Success Path: Update and Save
    data["skills"].append(new_skill)
    storage.save_json_file(data)
    print(f"Success: '{new_skill}' added and saved.")
    
def edit_skill(data):
    """Prompts, validates, and edits an existing skill."""
    skills = data.get("skills", [])
    
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
    # if index is not None    
    new_skill_name = input("Enter the new skill name: ").strip().lower()
    if validators.empty_input_checker(new_skill_name):
        print("Skill name can not be empty.")
        return         
    # Duplicacy prevention
    if new_skill_name in skills and  skills[index] != new_skill_name:
        print("Skill already exists.")
        return          
    # Editing skill and saving it to the system
    old_skill = skills[index]
    data["skills"][index] = new_skill_name
    #save
    storage.save_json_file(data)
    print(f"Success: '{old_skill}' updated to '{new_skill_name}' and saved.")   
    
           
def delete_skill(data):
    """Prompts, validates, and deletes an existing skill."""
    skills = data.get("skills", [])
    
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
    confirmation = input(f"Are you sure you want to delete this skill: {skill_name}. Type: ('Y' for yes OR 'N' for no): ").strip().lower()        
    if confirmation == 'n':
        print("Exiting the deletion process...")
        return
    elif confirmation == 'y':
        # deletion
        skills.pop(index)            
        # save
        storage.save_json_file(data)            
        print(f"Success: {skill_name} has been deleted.")            
    else:
        print("Invalid input for the confirmation.")
        return