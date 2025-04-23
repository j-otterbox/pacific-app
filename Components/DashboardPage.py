import constants as c
from Models.DashboardPageModel import DashboardPageModel
from Views.DashboardPageView import DashboardPageView
from Modules.EventManager import EventManager
from Components.ProjectForm import ProjectForm
from Modules.GuiManager import Modal, ContentWindow, Item

class DashboardPage:
    def __init__(self):
        self._model = DashboardPageModel()
        self._view = DashboardPageView()
        self.events = EventManager()
    
        self._view.set_new_project_menu_item_callback(self._new_project_menu_item_handler)

    def _new_project_menu_item_handler(self):
        
        
        Item.delete_children(c.MODAL)
        Item.set_label(c.MODAL, "Create New Project")
        project_form = ProjectForm(parent=c.MODAL)
        project_form.events.subscribe("new_project_created", self)
        project_form.render()

    def update(self, event:dict):
        data = event["data"]

        if event["type"] == "login_success":
            print(f"username '{data["username"]}' has logged in.")
            ContentWindow.clear()
            self._view.render(parent=c.CONTENT_WINDOW)
            
        elif event["type"] == "new_project_created":
            self.events.emit(event)

        elif event["type"] == "close_project":
            ContentWindow.clear()
            self._view.render(c.CONTENT_WINDOW)

            # a project list item with the data from the new item