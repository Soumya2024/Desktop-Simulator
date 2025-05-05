import tkinter as tk
from tkinter import Scale

class TemperatureControl:
    def __init__(self, parent):
        tk.Label(parent, text="Set Room Temperature").pack()
        self.scale = Scale(parent, from_=16, to=30, orient='horizontal', command=self.on_change)
        self.scale.set(22)
        self.scale.pack()

    def on_change(self, val):
        print(f"Temperature set to: {val}°C")
