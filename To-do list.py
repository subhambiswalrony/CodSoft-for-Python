''' Write a program in Python to create Simple To-Do List in Python (GUI using Tkinter) '''

import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_task = tk.Entry(frame)
entry_task.pack(fill=tk.X)

button_add = tk.Button(frame, text="Add Task", command=add_task)
button_add.pack(fill=tk.X)

button_delete = tk.Button(frame, text="Delete Task", command=delete_task)
button_delete.pack(fill=tk.X)

listbox_tasks = tk.Listbox(root)
listbox_tasks.pack(padx=10, pady=10)

root.mainloop()
