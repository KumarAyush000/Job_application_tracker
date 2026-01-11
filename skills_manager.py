import storage

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
    if not skills:
        print("Your skills list is currently empty.")
    else:
        print("Your Skills:")
        for idx, skill in enumerate(skills, 1):
            print(f"{idx}. {skill}")


def add_skill(data):
    """Prompts, validates, and adds a unique skill."""
    new_skill = input("Enter the skill to add: ").strip().lower()
    skills = data.get("skills", [])
    
    # empty input check
    if not new_skill:
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
    
    if not isinstance(skills, list) or not skills:
        print("Your skills list is currently empty or invalid. Nothing to edit.")
        return
    
    skill_to_edit = input("Enter the index number of the skill you want to edit: ").strip()
    
    # empty input check
    if not skill_to_edit:
        print("Index can not be empty.")
        return
    
    
    if skill_to_edit.isdigit():
          skill_to_edit = int(skill_to_edit)
          
          if 0 < skill_to_edit <= len(skills):
              new_skill_name = input("Enter the new skill name: ").strip().lower()
              if not new_skill_name:
                  print("Skill name can not be empty.")
                  return
              
              # Duplicacy prevention
              current_index = skill_to_edit -1
              if new_skill_name in skills and  skills[current_index] != new_skill_name:
                  print("Skill already exists.")
                  return
              
              # Editing skill and saving it to the system
              old_skill = skills[current_index]
              data["skills"][current_index] = new_skill_name
    
              #save
              storage.save_json_file(data)
              print(f"Success: '{old_skill}' updated to '{new_skill_name}' and saved.")   
              
          else:
              print(f"Index out of range. Choose between 1 and {len(skills)}.")
    else:
        print("Please enter a correct input for index.")
    
    
       

    
    
def delete_skill(data):
    pass
    