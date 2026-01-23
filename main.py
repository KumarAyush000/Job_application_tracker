import core.storage as storage
import services.candidate_manager as candidate_manager
import services.skills_manager as skills_manager
import services.auth_manager as auth_manager

def start_app():
    # 1. Load the data
    data = storage.load_json_file()
    # 2. Session state
    current_user_id = None

    # onboarding check
    if data.get("candidate") is None:
        candidate_manager.onboard_candidate(data)

    while True:
        print("\n----DASHBOARD----")

        if current_user_id is None:
            print("1. Create User")
            print("2. Login User")
            print("3. Exit")

            choice = input("Select an option: ").strip()

            if choice == "1":
                # Create new user
                auth_manager.create_user(data)

            elif choice == "2":
                # Login existing user
                user_id = auth_manager.login_user(data)
                if user_id:
                    current_user_id = user_id
            elif choice == "3":
                print("Exiting application...")
                break

            else:
                print("Invalid choice. Please select a valid option.")
        else:
            print(f"Logged in as: {current_user_id}")
            print("1. Manage Skills")
            print("2. Logout")
            print("3. Exit")

            choice = input("Select an option: ").strip()

            if choice == "1":
                skills_manager.manage_skills(data, current_user_id)
            
            elif choice == "2":
                # confirmation
                confirm = input("Are you sure you wnat to logout? (y/n): ").strip().lower()
                if confirm == "y":
                    current_user_id = None
                    print("Logged out successfully.")

            elif choice == "3":
                print("Exiting application...")
                break

            else:
                print("Invalid choice.")

if __name__ == "__main__":
    start_app()
