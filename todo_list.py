import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple To-Do List")

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Entry field for adding tasks
        self.task_entry = tk.Entry(self.root, width=35)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task button
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox to display tasks
        self.tasks_listbox = tk.Listbox(self.root, width=50, height=10, selectmode=tk.SINGLE)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Delete Task button
        self.delete_button = tk.Button(self.root, text="Delete Selected Task", command=self.delete_task)
        self.delete_button.grid(row=4, column=0, padx=10, pady=10)

        # Clear List button
        self.clear_button = tk.Button(self.root, text="Clear List", command=self.clear_tasks)
        self.clear_button.grid(row=4, column=1, padx=10, pady=10)

        # Task Completed button
        self.complete_button = tk.Button(self.root, text="Task Completed", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        # Task Incomplete button
        self.incomplete_button = tk.Button(self.root, text="Task Incomplete", command=self.incomplete_task)
        self.incomplete_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        """Adds a new task."""
        task = self.task_entry.get()
        if task:
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def delete_task(self):
        """Deletes the selected task."""
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.tasks_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def clear_tasks(self):
        """Clears all tasks."""
        self.tasks_listbox.delete(0, tk.END)

    def complete_task(self):
        """Marks the selected task as completed."""
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.tasks_listbox.itemconfig(selected_task_index, {'fg': 'green'})
            self.tasks_listbox.selection_clear(0, tk.END)  # Clear selection
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed!")

    def incomplete_task(self):
        """Marks the selected task as incomplete."""
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.tasks_listbox.itemconfig(selected_task_index, {'fg': 'red'})
            self.tasks_listbox.selection_clear(0, tk.END)  # Clear selection
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as incomplete!")

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
