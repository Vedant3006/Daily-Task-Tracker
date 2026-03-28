# 📝 Daily Task Tracker (CLI)

**Developer:** Vedant Sunil Patil  
**Registration Number:** 24BAI10122  
**Course:** Python Essentials Evaluated Course Project  
## 📌 About The Project
In the fast-paced life of a university student, keeping track of daily assignments, project deadlines, and personal chores can be highly overwhelming. Relying purely on memory often leads to uncompleted tasks and increased stress. 

To solve this real-world productivity problem, I developed the **Daily Task Tracker**—a lightweight, distraction-free Command-Line Interface (CLI) application built purely in Python. It acts as a digital To-Do list that runs directly in the terminal, allowing users to quickly log, view, and manage their daily tasks efficiently without the distraction of heavy GUI applications.

## ✨ Key Features
* **Continuous Interactive Menu:** Utilizes an infinite `while` loop to maintain a continuous session until the user explicitly chooses to exit.
* **Dynamic Task Management:** Users can instantly add new tasks to their list during runtime.
* **Real-time Task Viewing:** Displays all pending tasks cleanly, numbered automatically for better readability.
* **Task Completion & Removal:** Users can mark tasks as completed by deleting them via their specific index number.
* **Robust Error Handling:** Built-in validation checks to prevent crashes if a user inputs invalid data (e.g., typing a letter instead of a number).

## 💻 Technical Concepts Applied
This project demonstrates the practical application of core Python concepts learned in the course:
* **Data Structures:** Using `Lists` (`[]`) to dynamically store and manage strings (tasks).
* **Control Flow:** `if-elif-else` branching to navigate the user menu.
* **Loops:** `while True:` for the main application loop and iteration methods.
* **Built-in Functions:** `enumerate()`, `append()`, `pop()`, `len()`, and `int()`.
* **Exception Handling:** `try-except` blocks to handle `ValueError` inputs gracefully.

## ⚙️ Getting Started

### Prerequisites
To run this application, you only need Python installed on your system.
* Python 3.x (Download from [python.org](https://www.python.org/))

### Installation & Execution
1. Clone this repository or download the `task_tracker.py` source code file.
2. Open your computer's Terminal, Command Prompt, or VS Code.
3. Navigate to the directory where the file is saved.
4. Execute the script using the following command:
   ```bash
   python task_tracker.py

### Output
=========================================
   Welcome to your Daily Task Tracker!   
=========================================

Main Menu:
1. View Current Tasks
2. Add a New Task
3. Remove a Completed Task
4. Exit Application

Enter your choice (1/2/3/4): 2
Enter the task you want to add: Complete Python BYOP Project
-> Successfully added: 'Complete Python BYOP Project'

Enter your choice (1/2/3/4): 1
--- Your Pending Tasks ---
1. Complete Python BYOP Project
