import core.storage as storage
import services.candidate_manager as candidate_manager
import services.skills_manager as skills_manager


def start_app():
    data = storage.load_json_file()
    current_user_id = None  # runtime login state
    while True:
        print("\n---- MAIN DASHBOARD ----")
        print("1. Create User")
        print("2. Login User")
        print("3. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            # User creation flow (does NOT log the user in)
            candidate_manager.create_user(data)

        elif choice == "2":
            # Login flow
            user_id = candidate_manager.login_user(data)

            if user_id:
                current_user_id = user_id
                skills_manager.manage_skills(data, current_user_id)

        elif choice == "3":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    start_app()
