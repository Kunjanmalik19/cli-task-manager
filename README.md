# 📋 Console Task Manager

A lightweight, terminal-based Command Line Interface (CLI) Task Management application built in Python. This project demonstrates core Object-Oriented Programming (OOP) design principles, clean exception handling, and local file data persistence.

---

## ✨ Features
* **Create (Add Tasks):** Dynamically instantiate new tasks with custom titles and descriptions.
* **Read (View Tasks):** Display a structured list of ongoing tasks alongside their real-time statuses.
* **Update (Complete Tasks):** Safely locate and mark specific tasks as "Completed" by index mapping.
* **Delete (Remove Tasks):** Permanently clear tasks out of your records.
* **Data Persistence:** Automatically saves and extracts task states to/from a local `tasks.json` file.

---

## 🛠️ Tech Stack & Key Concepts Used
* **Language:** Python 3
* **Object-Oriented Programming (OOP):** Designed with clean data capsulation models using class structures.
* **File Handling & JSON Parsing:** Utilizes native `json` data serialization (`json.load` and `json.dump`) to safely map file structures to Python dictionaries.
* **Robust Error Handling:** Features complete `try-except` blocks protecting user terminal inputs and intercepting `ValueError` or decoding failures.

---

## 🚀 How to Run the Application

1. **Clone the repository to your local machine:**
   ```bash
   git clone [https://github.com/Kunjanmalik19/cli-task-manager.git]
   
