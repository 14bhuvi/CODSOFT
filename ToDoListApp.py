import tkinter as tk
from tkinter import messagebox
#importing a module tkinter
class ToDoListApp:
    def _init_(self, master):
        self.master = master
        self.master.title("ONLY FOR YOU") #the string is the name of application

        self.tasks = []

        #needs for application
        self.master.config(bg="#800080")
        self.title_label = tk.Label(master, text="Your ToDo List", font=("Helvetica", 20), bg="pink") #the text string is the description for application
        self.title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        #the entry button
        self.task_entry = tk.Entry(master, width=40, font=("Helvetica", 12),bg="#ADD8E6")
        self.task_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        print("WELCOME!")
        #tab1
        self.add_button = tk.Button(master, text="Add Your Task", command=self.add_task, bg="#4CAF50", fg="black", font=("Helvetica", 12)) #using fg for font color
        self.add_button.grid(row=1, column=1, padx=5, pady=10, sticky="ew")                                                                #using bg for background colors for tabs
   
        self.task_listbox = tk.Listbox(master, width=50, height=15, font=("Helvetica", 12))
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        #tab2
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task, bg="red", fg="white", font=("Helvetica", 12))
        self.delete_button.grid(row=3, column=0, padx=5, pady=10, sticky="ew")
        #tab3
        self.update_button = tk.Button(master, text="Update Task", command=self.update_task, bg="#FFA500", fg="black", font=("Helvetica", 12))
        self.update_button.grid(row=3, column=1, padx=5, pady=10, sticky="ew")

        self.refresh_tasks()
    #define for the tabs or following steps for application 
    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task['title'])

    def add_task(self):
        task_title = self.task_entry.get()
        if task_title:
            self.tasks.append({'title': task_title})
            self.refresh_tasks()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.refresh_tasks()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            new_title = self.task_entry.get()
            if new_title:
                self.tasks[selected_index[0]]['title'] = new_title
                self.refresh_tasks()

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if _name_ == "_main_":
    main()
