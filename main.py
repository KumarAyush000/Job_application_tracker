import core.storage as storage
import services.candidate_manager as candidate_manager
import services.skills_manager as skills_manager

def start_app():
    # 1. Load the data
    data = storage.load_json_file()

    # 2. Session state
    current_user_id = None

    while True:
        print("\n----CANDIDATE DASHBOARD----")
        print("1. Create User")
        print("2. Login User")
        print("3. Manage Skills")
        print("4. Logout")
        print("5. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            # Create new user
            user_id = candidate_manager.create_user(data)
            if user_id:
                current_user_id = user_id
                print(f"Logged in as User ID: {current_user_id}")

        elif choice == "2":
            # Login existing user
            user_id = candidate_manager.login_user(data)
            if user_id:
                current_user_id = user_id
                print(f"Logged in as User ID: {current_user_id}")

        elif choice == "3":
            # HARD GUARD enforced inside skills manager
            skills_manager.manage_skills(data, current_user_id)

        elif choice == "4":
            # Logout
            if current_user_id is None:
                print("No user is currently logged in.")
            else:
                print(f"User {current_user_id} logged out.")
                current_user_id = None

        elif choice == "5":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    start_app()
