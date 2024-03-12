import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("Todo List")

# Create GUI components
entry_task = tk.Entry(root, width=50)
button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task)
listbox_tasks = tk.Listbox(root, height=10, width=50)

# Place GUI components on the window
entry_task.pack()
button_add_task.pack()
listbox_tasks.pack()
button_delete_task.pack()

# Start the main loop
root.mainloop()

