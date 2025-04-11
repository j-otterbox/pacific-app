from Events.EventManager import EventManager
from Views.DashboardView import DashboardView
from Util import named_items

class DashboardController:
    def __init__(self):
        self.events = EventManager()
        self._view = DashboardView()

        project_form = self._view.get_project_form()
        project_form.events.subscribe("new_project_created", self)

    def update(self, data:dict):
        if data["event_type"] == "login_success":
            print(f"username '{data["username"]}' has logged in.")
            content_window = named_items.content_window.value
            self._view.render(parent=content_window)

        # create new project list item with item data
        if data["event_type"] == "new_project_created":
            print("new project item was created") 