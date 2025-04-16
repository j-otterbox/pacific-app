import constants as c
from Modules.EventManager import EventManager
from Views.DashboardPageView import DashboardPageView
from Controllers.ProjectFormController import ProjectFormController
from Modules.GuiManager import Modal


class DashboardPageController:
    def __init__(self):
        self.events = EventManager()
        self._view = DashboardPageView()
    
        self._view.set_new_project_menu_item_callback(self._new_project_menu_item_handler)

    def _new_project_menu_item_handler(self):
        project_form = ProjectFormController()
        project_form.events.subscribe("new_project_created", self)
        stage_id = project_form.get_stage_id()
        Modal.set_title("Create New Project")
        Modal.set_content(stage_id)
        Modal.show()

    def update(self, event:dict):
        data = event["data"]

        if event["type"] == "login_success":
            print(f"username '{data["username"]}' has logged in.")
            self._view.render(parent=c.CONTENT_WINDOW)
            
        if event["type"] == "new_project_created":
            self.events.emit(event)

            # a project list item with the data from the new item