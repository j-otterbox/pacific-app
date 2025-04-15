import constants as c
from Modules.EventManager import EventManager
from Views.DashboardPageView import DashboardPageView
from collections.abc import Callable
from Controllers.ProjectFormController import ProjectFormController


class DashboardPageController:
    def __init__(self):
        self.events = EventManager()
        self._view = DashboardPageView()
    
        self._view.set_new_project_menu_item_callback(self._new_project_menu_item_handler)

    def _new_project_menu_item_handler(self):
        self._view.set_modal_label("Create New Project")
        self._project_form.render()
        self._view.show_modal()

    def update(self, data:dict):
        if data["event_type"] == "login_success":
            print(f"username '{data["username"]}' has logged in.")
            self._view.render(parent=c.CONTENT_WINDOW)
            
        if data["event_type"] == "new_project_created":
            print("new project item was created")