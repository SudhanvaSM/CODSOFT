import tkinter as tk
from tkinter import messagebox

# Class representing each task's status.
class Status:

    # Initializing task's status as not completed.
    def __init__(self,descr):
        self.descr = descr
        self.completed = False

    def mark_completed(self):
        self.completed = True

    # Return a string representation of the task's status.
    def __str__(self):
        status = '✔' if self.completed else 'X'
        return f"[{status}] {self.descr}"

# Main application class for the To-Do list.
class ToDoApp:

    # Initialize the GUI application and its elements.
    def __init__(self,main):
        self.main = main
        self.main.title("TO-DO List App")
        self.tasks = []

        # Title label with font style.
        self.label = tk.Label(main,text = "To-Do List", font = ("Times New Roman", 20, "bold underline"))
        self.label.pack()

        # Listbox to display tasks.
        self.listbox = tk.Listbox(main, height=10, width=60, selectmode=tk.SINGLE)
        self.listbox.pack(padx=10,pady=10)

        # Entry widget to input task descriptions.
        self.entry = tk.Entry(main,width=60)
        self.entry.pack(pady=10)

        # Frame to contain all the buttons.
        self.button_frame = tk.Frame(main)
        self.button_frame.pack(pady=5)

        # Button to add new tasks to the list.
        self.add_button = tk.Button(self.button_frame, text="Add Task", width=15, command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10,pady=10)

        # Button to remove tasks from the list.
        self.add_button = tk.Button(self.button_frame, text="Remove Task", width=15, command=self.remove_task)
        self.add_button.pack(side=tk.LEFT, padx=10,pady=10)

        # Button to mark tasks as completed in the list.
        self.add_button = tk.Button(self.button_frame, text="Complete Task", width=15, command=self.complete_task)
        self.add_button.pack(side=tk.LEFT, padx=10,pady=10)

        # Update the listbox to show current tasks.
        self.update_listbox()

    # Method to add a new task to the task list.
    def add_task(self):
        task = self.entry.get()
        if task != "":  # Check if task description is not empty.
            new_task = Status(task) # Create new task obejct in Status class.
            self.tasks.append(new_task) # Add new task into the list.
            self.update_listbox()   # Up
            self.entry.delete(0,tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")   # Show warning if input is empty.
        
    # Method to remove existing task from the task list.
    def remove_task(self):
        try:
            task_num = self.listbox.curselection()[0]
            self.tasks.pop(task_num)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    # Method to mark a task as completed in the task list.
    def complete_task(self):
        try:
            task_num = self.listbox.curselection()[0]
            self.tasks[task_num].mark_completed()
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    # Method to update the listbox with the current tasks.
    def update_listbox(self):
        self.listbox.delete(0,tk.END)
        tasks = [str(task) for task in self.tasks]
        for task in tasks:
            self.listbox.insert(tk.END,task)

# Main function to run the Tkinter application.
def main():
    main = tk.Tk()
    app = ToDoApp(main)
    main.mainloop()

# Check if the script is run directly (not imported).
if __name__ == "__main__":
    main()