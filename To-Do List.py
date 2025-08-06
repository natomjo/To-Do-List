import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def load_tasks():
    try:
        with open("file.txt", 'r') as f:
            tasks = f.readlines()
            for task in tasks:
                task = task.strip()
                if task.startswith("[COMPLETED] "):
                    task_text = task[12:]
                    listbox_tasks.insert(tk.END, task_text)
                    listbox_tasks.itemconfig(tk.END, fg = 'gray')
                else:
                    listbox_tasks.insert(tk.END, task)
    except FileNotFoundError:
        pass        

def save_tasks():
    with open("file.txt", 'w') as f:
        for i in range(listbox_tasks.size()):
            task = listbox_tasks.get(i)
            fg_color = listbox_tasks.itemcget(i, 'fg')
            if fg_color == 'gray':
                f.write(f"[COMPLETED] {task}\n")
            else:
                f.write(f"{task}\n")

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        if messagebox.askyesno("Confirm", "Are you sure you want to delete the tasks?"):
            selected_task = listbox_tasks.curselection()[0]
            listbox_tasks.delete(selected_task)
            save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_completed():
    try:
        selected_task = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(selected_task, fg = 'gray')
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def clear_all():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        listbox_tasks.delete(0, tk.END)
        save_tasks()

def on_closing():
    save_tasks()
    if messagebox.askyesno("Confirm", "Are you sure you want to exit?"):    
        root.destroy()        

root=tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.configure(bg="silver")

frame_entry = tk.Frame(root)
frame_entry.pack(pady=10)

entry_task = tk.Entry(frame_entry, width=30)
entry_task.pack(side=tk.LEFT, padx=5)

button_add = tk.Button(frame_entry, text=" Add Task ", command=add_task, bg="lightblue", fg="blue")
button_add.pack(side=tk.LEFT)

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, width=50, height=15, font=('Arial', 10))
listbox_tasks.pack(side=tk.LEFT)

style = ttk.Style()
style.theme_use("default")
style.configure("Vertical.TScrollbar", troughcolor="maroon", arrowsize=15)

scrollbar_tasks = ttk.Scrollbar(frame_tasks, orient=tk.VERTICAL, command=listbox_tasks.yview)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview, style="Vertical.TScrollbar")

frame_controls = tk.Frame(root)
frame_controls.pack(pady=10)

button_delete = tk.Button(frame_controls, text=" Delete Task ", command=delete_task, bg="pink", fg="red")
button_delete.pack(side=tk.LEFT, padx=5)

button_complete = tk.Button(frame_controls, text=" Mark Completed ", command=mark_completed, bg="lightgreen", fg="green")
button_complete.pack(side=tk.LEFT, padx=5)

button_clear = tk.Button(frame_controls, text=" Clear All ", command=clear_all, bg="lightgray", fg="gray")
button_clear.pack(side=tk.LEFT, padx=5)

load_tasks()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()