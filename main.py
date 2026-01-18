import core.storage as storage
import services.candidate_manager as candidate_manager
import services.skills_manager as skills_manager


def start_app():
    data = storage.load_json_file()
    current_user_id = None  # runtime login state
    while True:
        print("\n----CANDIDATE DASHBOARD----")

        if current_user_id is None:
            print("1. Create User")
            print("2. Login User")
            print("3. Exit")
        else:
            print(f"Logged in as: {current_user_id}")
            print("1. Manage Skills")
            print("2. Logout")
            print("3. Exit")

        choice = input("Select an option: ").strip()

        # NOT LOGGED IN
        if current_user_id is None:
            if choice == "1":
                candidate_manager.create_user(data)
            elif choice == "2":
                current_user_id = candidate_manager.login_user(data)
            elif choice == "3":
                print("Exiting application...")
                break
            else:
                print("Invalid choice.")

        # LOGGED IN
        else:
            if choice == "1":
                skills_manager.manage_skills(data, current_user_id)
            elif choice == "2":
                print("Logging out...")
                current_user_id = None
            elif choice == "3":
                print("Exiting application...")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    start_app()
