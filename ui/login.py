# import tkinter as tk
# from tkinter import messagebox
# from ui.dashboard import Dashboard

# class LoginWindow:
#     def __init__(self, root):
#         self.root = root
#         self.frame = tk.Frame(self.root)
#         self.frame.pack()

#         tk.Label(self.frame, text="Username").pack()
#         self.username = tk.Entry(self.frame)
#         self.username.pack()

#         tk.Label(self.frame, text="Password").pack()
#         self.password = tk.Entry(self.frame, show="*")
#         self.password.pack()

#         tk.Button(self.frame, text="Login", command=self.authenticate).pack()

#     def authenticate(self):
#         user = self.username.get()
#         pw = self.password.get()
#         if user == "admin" and pw == "admin":
#             self.frame.destroy()
#             Dashboard(self.root)
#         else:
#             messagebox.showerror("Login Failed", "Invalid credentials.")

import tkinter as tk
from tkinter import messagebox
from ui.dashboard import Dashboard
from backend.auth_db import authenticate_user, register_user, init_db

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=100)

        init_db()  # Ensure the DB is initialized

        tk.Label(self.frame, text="Username").pack()
        self.username = tk.Entry(self.frame)
        self.username.pack()

        tk.Label(self.frame, text="Password").pack()
        self.password = tk.Entry(self.frame, show="*")
        self.password.pack()

        tk.Button(self.frame, text="Login", command=self.authenticate).pack(pady=5)
        tk.Button(self.frame, text="Register", command=self.register).pack()

    def authenticate(self):
        user = self.username.get()
        pw = self.password.get()

        if authenticate_user(user, pw):
            messagebox.showinfo("Login Success", f"Welcome, {user}!")
            self.frame.destroy()
            Dashboard(self.root)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def register(self):
        user = self.username.get()
        pw = self.password.get()

        if not user or not pw:
            messagebox.showerror("Error", "Please fill both fields.")
            return

        if register_user(user, pw):
            messagebox.showinfo("Success", "Registration complete. You can now login.")
        else:
            messagebox.showerror("Error", "Username already exists.")
