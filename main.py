import tkinter as tk
from ui.login import LoginWindow

def run_app():
    root = tk.Tk()
    root.title("Smart Home Control Panel")
    root.geometry("800x600")
    app = LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
