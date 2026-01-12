# Skill Tracker CLI Application

## Description

A command-line application for managing personal skills using clean, modular Python code. The application supports full CRUD operations, robust input validation, and persistent storage using JSON.

This project is designed to demonstrate real-world Python programming practices such as separation of concerns, reusable validation logic, and safe user input handling.

---

## Features

* Add, edit, and delete skills
* Index-based selection with safe error handling
* Reusable input and index validation helpers
* Persistent data storage using JSON
* Clean, modular project architecture

---

## Technologies Used

* Python
* JSON
* Modular programming principles
* Unit-test mindset (logic written to be testable)

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
├── main.py          # Application entry point
├── services/        # Business logic and storage handling
├── validators/      # Reusable input and index validation helpers
├── data/            # Persistent JSON storage
└── README.md
```

---

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

