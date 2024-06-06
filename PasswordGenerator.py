import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        password_length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length")
        return
    
    if password_length <= 7:
        messagebox.showerror("Error", "Password length must be at least 8")
        return
    
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_length))
    password_label.config(text=password)


root = tk.Tk()
root.title("Security first! PASSWORD GENERATOR")


window_width = 500
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")


root.config(bg="#900C3F")


input_frame = tk.Frame(root, bg="black")
input_frame.pack(pady=20)


length_label = tk.Label(input_frame, text="Enter required length for password:\n[length must be atleast 8]", font=("Arial", 12), bg="#808000")
length_label.grid(row=1, column=0, padx=10)
length_entry = tk.Entry(input_frame, font=("Arial", 12))
length_entry.grid(row=1, column=1, padx=10)


output_frame = tk.Frame(root, bg="#008080")
output_frame.pack(pady=20)


password_label = tk.Label(output_frame, text="", font=("Arial", 16), bg="#C0C0C0")
password_label.pack(pady=10)


generate_button = tk.Button(output_frame, text="Generate Password", font=("Italic Arial", 12), command=generate_password)
generate_button.pack()

root.mainloop()

