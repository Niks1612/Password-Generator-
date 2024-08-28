import tkinter as tk
import random
import string

def generate_password():
    length = int(password_length.get())
    if use_numbers_and_characters.get():
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


root = tk.Tk()
root.title("Password Generator")

# Set window size
root.geometry("350x200")  # Width x Height

# Variables
use_numbers_and_characters = tk.BooleanVar(value=True)
password_length = tk.StringVar(value="10")

# UI Elements
tk.Radiobutton(root, text="Use numbers and characters", variable=use_numbers_and_characters, value=True).pack(anchor='w')
tk.Radiobutton(root, text="Letters only", variable=use_numbers_and_characters, value=False).pack(anchor='w')

length_frame = tk.Frame(root)
length_frame.pack(anchor='w')

tk.Label(length_frame, text="Password length:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(length_frame, textvariable=password_length).grid(row=0, column=1, padx=5, pady=5)

password_frame = tk.Frame(root)
password_frame.pack(anchor='w', pady=10)

tk.Button(password_frame, text="Generate", command=generate_password).pack(side='left', padx=5)
password_entry = tk.Entry(password_frame, font=('Arial', 12), justify='center')
password_entry.pack(side='left')

# Run the main loop
root.mainloop()
