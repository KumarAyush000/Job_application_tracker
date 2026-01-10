import storage
import candidate_manager
import skills_manager
def start_app():
    # 1. Load the data (storage.py handles disk details)
    data = storage.load_json_file()

    # 2. THE DIRECT CHECK: This is your binary decision point
    # We use .get() to ask "Is there data inside this key?"
    if data.get("candidate") is None:
        # PATH A: The "fresh start" flow
        print("CANDIDATE CHECK: Missing (None)")
        print("ACTION: Starting onboarding process...")
        candidate_manager.onboard_candidate(data)
                    
    else:
        # PATH B: The "resume" flow
        print(f"CANDIDATE CHECK: Present ({data['candidate']})")
        print("ACTION: Skipping onboarding. Loading dashboard...")
        # load_existing_dashboard(data)
        
    # Dashboard visibility
    while True:
        print("\n----CANDIDATE DASHBOARD----")
        print("1. Manage Skills")
        print("2. Exit")
            
        choice = input("Select an option: ").strip()
            
        if choice == "1":
            skills_manager.manage_skills(data)
        elif choice =="2":
            print("Exiting Dashboard...")
            break
        else:
            print("Invalid choise. Please select 1 or 2.")

if __name__ == "__main__":
    start_app()
