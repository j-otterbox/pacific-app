from Models.ProjectModel import ProjectModel
from Views.ProjectFormView import ProjectFormView
from Modules.EventManager import EventManager

class ProjectFormController:
    def __init__(self):
        self._model = ProjectModel()
        self._view = ProjectFormView()
        self.events = EventManager()

        self._view.set_create_btn_callback(self._create_btn_click_handler)

    def set_parent(self, parent:int|str):
        self._parent = parent
        
    # complete this function
    def _create_btn_click_handler(self):
        form_data = self._view.get_form_data()
        if self._model.validate(form_data):
            print("form validated")
            resp = self._model.create_project(form_data)
            if resp["success"]:
                self.events.emit("new_project_created", resp)
            else:
                if resp["msg"] == "job_id conflict":
                    self._view.set_feedback_text("A project already exists with the given ID.")
                    self._view.highlight_input("job_id")
                elif resp["msg"] == "name conflict":
                    self._view.set_feedback_text("A project already exists with the given name.")
                    self._view.highlight_input("name")
                self._view.show_feedback()
        else:
            for key, value in form_data.items():
                print(key, value)
                if value == "":
                    self._view.highlight_input(key)

    def render(self) -> None:
        print("render proj form")
        self._view.render(self._parent)




        
