import storage

def start_app():
    # 1. Load the data (storage.py handles disk details)
    data = storage.load_json_file()

    # 2. THE DIRECT CHECK: This is your binary decision point
    # We use .get() to ask "Is there data inside this key?"
    if data.get("candidate") is None:
        # PATH A: The "fresh start" flow
        print("CANDIDATE CHECK: Missing (None)")
        print("ACTION: Starting onboarding process...")
        # setup_new_candidate(data)
    else:
        # PATH B: The "resume" flow
        print(f"CANDIDATE CHECK: Present ({data['candidate']})")
        print("ACTION: Skipping onboarding. Loading dashboard...")
        # load_existing_dashboard(data)

if __name__ == "__main__":
    start_app()
