import constants as c
from Models.ProjectPageModel import ProjectPageModel
from Views.ProjectPageView import ProjectPageView
from Modules.EventManager import EventManager
from Modules.GuiManager import ContentWindow

class ProjectPage:
    def __init__(self):
        self._model = ProjectPageModel()
        self._view = ProjectPageView()
        self.events = EventManager()

        self._view.set_dashboard_btn_callback(self._dashboard_btn_click_handler)

    def logout_btn_click_handler():
        pass

    def _dashboard_btn_click_handler(self):
        self.events.emit({
            "type": "close_project",
            "data": None
        })

    def update(self, event:dict):
        # for key, value in event.items():
        #     print(key, value)

        if event["type"] == "new_project_created":
            ContentWindow.clear()
            self._view.render(parent=c.CONTENT_WINDOW)
            

        