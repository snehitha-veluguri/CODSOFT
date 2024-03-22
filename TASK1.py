#Create a Todo List in Python

from tkinter import *

# Initialize the window
root = Tk()
root.geometry("400x400")
root.title("Todo List")

# Create a list to hold the tasks
tasks = []

# Add task function
def add_task():
    # Get the task from the entry box
    task = entry_task.get()
    
    # Add the task to the list and 
    # clear the entry box
    if task != "":
        tasks.append(task)
        entry_task.delete(0, END)
        
        # Update the task list
        update_tasks()

# Remove task function
def remove_task():
    # Get the selected task
    selected_task = list_tasks.curselection()[0]
    
    # Remove the task from the list 
    # and update the task list
    del tasks[selected_task]
    update_tasks()

# Update task list function
def update_tasks():
    # Clear the task list
    list_tasks.delete(0, END)
    
    # Add the tasks to the list
    for task in tasks:
        list_tasks.insert(END, task)

# Create the GUI elements
label_task = Label(root, text="Task:")
label_task.pack()

entry_task = Entry(root)
entry_task.pack()

button_add = Button(root, 
text="Add Task", command=add_task)
button_add.pack()

button_remove = Button(root, 
text="Remove Task", command=remove_task)
button_remove.pack()

list_tasks = Listbox(root)
list_tasks.pack()

# Run the main loop
root.mainloop()