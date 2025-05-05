import tkinter as tk
from tkinter import ttk
from ui.components.room_control import RoomControl
from ui.components.temperature_control import TemperatureControl
from ui.components.theme_toggle import ThemeToggle
from ui.components.analytics import AnalyticsTab

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.tab_control = ttk.Notebook(root)

        self.living_room_tab = ttk.Frame(self.tab_control)
        self.bedroom_tab = ttk.Frame(self.tab_control)
        self.settings_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.living_room_tab, text="Living Room")
        self.tab_control.add(self.bedroom_tab, text="Bedroom")
        self.tab_control.add(self.settings_tab, text="Settings")

        self.tab_control.pack(expand=1, fill='both')

        RoomControl(self.living_room_tab, "Living Room")
        TemperatureControl(self.bedroom_tab)
        ThemeToggle(self.settings_tab)
        
        self.analytics_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.analytics_tab, text="Analytics")
        AnalyticsTab(self.analytics_tab)


