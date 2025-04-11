from Events.EventManager import EventManager
from Views.DashboardView import DashboardView
from Util import named_items

class DashboardController:
    def __init__(self):
        self.events = EventManager()
        self._view = DashboardView()

    def update(self, data:dict):
        if data["event_type"] == "login_success":
            print(f"user '{data["username"]}' has logged in.")
            content_window = named_items.content_window.value
            self._view.render(parent=content_window)
