import tkinter as tk
from tkinter import messagebox, font

# task list
task_list = []

#Add new task
def add_task():
    title = entry.get().strip()
    if title:
        task = {"title":title, "status": "incomplete"}
        task_list.append(task)
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Warning","⚠Please enter a task!")

# Mark  task as complete
def complete_task(event=None):
    try:
        index = listbox.curselection()[0]
        task_list[index]["status"] = "Complete"
        update_listbox()
    except IndexError:
        messagebox.showerror("Error","❌Please select a task!")

        #Delete selected task
def delete_task():
    try:
        index = listbox.curselection()[0]
        del task_list[index]
        update_listbox()
    except IndexError:
        messagebox.showerror("Error","❌Please select a delete!")

# Refresh task list
def update_listbox():
    listbox.delete(0, tk.END)
    for i, task in enumerate(task_list):
        status_icon = "✔" if task["status"] == "Complete" else "⭕"
        listbox.insert(tk.END,f"{status_icon} {task['title']}")

    #GUI setup
root = tk.Tk()
root.title("Todo App by Iqra Arif")
root.geometry("460x520")
root.config(bg="#595963")

#Fonts
heading_font = ("Helvetica", 18, "bold")
task_font = ("Arial",12)
button_font = ("Arial",10, "bold")

# Heading
title_lable = tk.Label(root, text="To-do List by Iqra Arif", font=heading_font, bg="#362D2A", fg="#ffffff")
title_lable.pack(pady=15)

#Entry field
entry = tk.Entry(root, width=28, font=("Arial",13))
entry.pack(pady=10, ipady=5)

#Add button
add_btn = tk.Button(root, text="ADD", width=15, bg="#77B1D3", fg="white", font=button_font,command=add_task)
add_btn.pack(pady=5)

# Listbox for tasks
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=20)

listbox = tk.Listbox(listbox_frame, width=40, height=10, font=task_font, bg="#ffffff", fg="#333", selectbackground="#ff5c5c")
listbox.pack()

# Complete button
complete_btn = tk.Button(root, text="✔Mark Complete",bg="#8B2824", fg="white", font=button_font,width=20, command=complete_task)
complete_btn.pack(pady=5)

# Delete button
delete_btn = tk.Button(root, text="🗑Delete Task",bg="#6b2c61", fg="white", font=button_font,width=20, command=delete_task)
delete_btn.pack(pady=5)

#Footer
footer = tk.Label(root, text="Developed by Iqra Arif",font=("Arial",10),fg="#888",bg="#2A4749")
footer.pack(side="bottom", pady=10)

#Bind enter key
root.bind('<Return>', lambda event:add_task())

#Run App
root.mainloop()