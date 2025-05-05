import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import csv
from datetime import datetime

class AnalyticsTab:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.pack(expand=True, fill='both')
        self.draw_graph()

    def draw_graph(self):
        timestamps, devices = [], []

        try:
            with open('data/logs/usage_log.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    timestamps.append(datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f'))
                    devices.append(row[1])
        except FileNotFoundError:
            return

        # Simple usage count per device
        device_counts = {}
        for device in devices:
            device_counts[device] = device_counts.get(device, 0) + 1

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.bar(device_counts.keys(), device_counts.values())
        ax.set_title("Device Usage Count")
        ax.set_ylabel("Usage")

        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
