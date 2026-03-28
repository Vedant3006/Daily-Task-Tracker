"""
Project: Daily Task Tracker (CLI To-Do List)
Developer: Vedant Sunil Patil (Reg No. 24BAI10122)
Course: Python Essentials Evaluated Course Project
Description: An interactive CLI application to Add, View, and Remove daily tasks.
"""

def main():
    # CONCEPT: Using a List to store data
    tasks = []
    
    print("=========================================")
    print("   Welcome to your Daily Task Tracker!   ")
    print("=========================================")

    # CONCEPT: Using a While loop for continuous interaction
    while True:
        print("\nMain Menu:")
        print("1. View Current Tasks")
        print("2. Add a New Task")
        print("3. Remove a Completed Task")
        print("4. Exit Application")
        
        # CONCEPT: Taking user choice
        choice = input("\nEnter your choice (1/2/3/4): ")
        
        # CONCEPT: Control Flow (if-elif-else)
        if choice == '1':
            if len(tasks) == 0:
                print("-> Your task list is completely empty. Enjoy your day!")
            else:
                print("\n--- Your Pending Tasks ---")
                # Using a for loop to display tasks with numbers
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                    
        elif choice == '2':
            new_task = input("Enter the task you want to add: ")
            tasks.append(new_task) # Adding to the list
            print(f"-> Successfully added: '{new_task}'")
            
        elif choice == '3':
            if len(tasks) == 0:
                print("-> No tasks available to remove!")
            else:
                try:
                    task_num = int(input("Enter the task number you completed: "))
                    # Checking if the number is valid
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1) # Removing from the list
                        print(f"-> Great job! '{removed_task}' has been removed.")
                    else:
                        print("-> Invalid task number. Please check the list and try again.")
                except ValueError:
                    print("-> Error: Please enter a valid numerical value!")
                    
        elif choice == '4':
            print("-> Saving changes... Exiting Task Tracker. Have a productive day!")
            break # Breaks the while loop to exit the program
            
        else:
            print("-> Invalid choice. Please select an option from 1 to 4.")

# Running the program
if __name__ == "__main__":
    main()
