import tkinter as tk

class ThemeToggle:
    def __init__(self, parent):
        self.parent = parent
        self.dark_mode = tk.BooleanVar()
        tk.Checkbutton(parent, text="Dark Mode", variable=self.dark_mode, command=self.toggle_theme).pack()

    def toggle_theme(self):
        if self.dark_mode.get():
            self.parent.configure(bg="black")
        else:
            self.parent.configure(bg="white")
