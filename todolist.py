import tkinter as tk
from tkinter import ttk


def add_task():
  task = task_entry.get()
  if task:
    tasks.append(task)
    list_update()
    task_entry.delete(0, tk.END)
  else:

    tk.messagebox.showinfo("Error", "Please enter a task.")


def list_update():
  task_listbox.delete(0, tk.END)
  for task in tasks:
    task_listbox.insert(tk.END, task)


def delete_task():
  try:
    selected_task_index = task_listbox.curselection()[0]
    tasks.pop(selected_task_index)
    list_update()
  except IndexError:

    tk.messagebox.showinfo("Error", "Please select a task to delete.")


window = tk.Tk()
window.title("To-Do List")

style = ttk.Style()
style.theme_use('clam')


tasks = []


task_entry = ttk.Entry(window, width=50)
task_entry.pack(pady=10)


add_button = ttk.Button(window, text="Add Task", command=add_task)
add_button.pack()


task_listbox = tk.Listbox(window, width=50)
task_listbox.pack()


delete_button = ttk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=10)


window.mainloop()

