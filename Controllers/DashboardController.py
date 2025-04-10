from Events.EventManager import EventManager
from Views.DashboardView import DashboardView

class DashboardController:
    def __init__(self):
        self.events = EventManager()
        self._view = DashboardView()

    def update(self, data:dict):
        if data["event_type"] == "on_login":
            self.render()

    def render(self, parent:int|str):
        pass