import tkinter as tk

class RoomControl:
    def __init__(self, parent, room_name):
        self.parent = parent
        tk.Label(parent, text=f"{room_name} Controls").pack()

        self.light_state = tk.BooleanVar()
        tk.Checkbutton(parent, text="Light", variable=self.light_state, command=self.toggle_light).pack()

        self.fan_state = tk.BooleanVar()
        tk.Checkbutton(parent, text="Fan", variable=self.fan_state, command=self.toggle_fan).pack()

    def toggle_light(self):
        print(f"Light is {'ON' if self.light_state.get() else 'OFF'}")

    def toggle_fan(self):
        print(f"Fan is {'ON' if self.fan_state.get() else 'OFF'}")
