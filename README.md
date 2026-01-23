# Skill Tracker CLI Application (Multi-User)

## Description

A command-line application for managing personal skills with **multi-user support**, built using clean, modular Python architecture.  
The application supports **user creation, login/logout, per-user skill management (CRUD)**, robust input validation, and persistent storage using JSON.

This project demonstrates **real-world Python programming practices** such as separation of concerns, session handling, defensive programming, and scalable data modeling.

---

## Features

- User creation and login system  
- Session-based access control (login required)  
- Per-user skill management (scoped data)  
- Add, edit, and delete skills  
- Index-based selection with safe error handling  
- Reusable input and index validation helpers  
- Persistent data storage using JSON  
- Clean, modular project architecture  
- Logic written with a **unit-test mindset**

---

## Technologies Used

- Python  
- JSON  
- Modular programming principles  
- Defensive programming  
- CLI-based application design 

---

## How to Run

1. Clone the repository
2. Navigate to the project directory
3. Run the application:

   ```bash
   python main.py
   ```

---

## Project Structure

```
.
├── main.py                # Application entry point (dashboard & session handling)
├── services/
│   ├── auth_manager.py    # User creation, login, user retrieval
│   ├── skills_manager.py  # Skill CRUD logic (per user)
│   └── candidate_manager.py
├── validators/            # Reusable input and index validation helpers
├── core/
│   └── storage.py         # JSON load/save logic
├── data/
│   └── data.json          # Persistent storage
└── README.md
```

---

## Application Flow (High-Level)

- Application loads persisted JSON data
- Candidate onboarding runs if required
- User can :
         - Create a new user
         - Log in Using User ID
- Once logged in :
         - Skills are managed only for that user
         - Access is bloced if not logged in
- All changes are saved persistently
## Real-World Motivation

Job seekers often apply to many companies simultaneously but struggle with:

* Tracking application status (Applied, Interview, Rejected, Offer)
* Remembering follow-ups
* Identifying missing skills for specific roles
* Improving their profile strategically instead of learning skills randomly

This project addresses the **organization and decision-making problem** using Python logic and structured data handling.

---

## Future Scope (Planned Enhancements)

> Note: The features below are **not yet implemented** and represent planned future enhancements.

* Track job applications and their statuses
* Analyze required skills across different roles
* Compare required skills with the user’s current skill set
* Recommend which skills to learn next to maximize interview chances

---

## What I Learned

* Designing user-friendly CLI workflows
* Writing reusable and defensive validation logic
* Managing persistent application state using JSON
* Structuring a Python project following real-world practices

---

