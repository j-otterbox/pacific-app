from Models.ProjectFormModel import ProjectFormModel
from Views.ProjectFormView import ProjectFormView
from Modules.EventManager import EventManager
from Modules.GuiManager import Modal

class ProjectFormController:
    def __init__(self):
        self._model = ProjectFormModel()
        self._view = ProjectFormView()
        self.events = EventManager()

        self._view.set_create_btn_callback(self._create_btn_click_handler)
        self._view.set_cancel_btn_callback(self._cancel_btn_click_handler)
        self._view.set_manage_pms_btn_callback(self._manage_pms_btn_click_handler)
        self._view.set_manage_gcs_btn_callback(self._manage_gcs_btn_click_handler)
        
    # complete this function
    def _create_btn_click_handler(self):
        form_data = self._view.get_form_data()
        if self._model.validate(form_data):
            resp = self._model.create_project(form_data)
            if resp["success"]:
                self.events.emit({
                    "type": "new_project_created",
                    "data": resp["data"]
                })
                Modal.hide()
                Modal.clear()
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

    def _manage_pms_btn_click_handler(self):
        print("manage project managers")

    def _manage_gcs_btn_click_handler(self):
        print("manage gen contractors")

    def _cancel_btn_click_handler(self):
        Modal.hide()
        Modal.clear()

    def get_stage_id(self):
        return self._view._stage_id