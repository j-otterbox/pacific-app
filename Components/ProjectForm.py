from Models.ProjectFormModel import ProjectFormModel
from Views.ProjectFormView import ProjectFormView
from Views.ListEditorView import ListEditorView
from Views.TextInputFormView import TextInputFormView
from Modules.EventManager import EventManager
from Modules.GuiManager import Modal

class ProjectForm:
    def __init__(self, parent:int|str):
        self.events = EventManager()
        self._project_form_model = ProjectFormModel()
        self._project_form_view = ProjectFormView(parent)
        self._list_editor_view = ListEditorView()
        self._text_input_form_view = TextInputFormView()
        
        GCs = self._project_form_model.get_GCs(names_only=True)
        PMs = self._project_form_model.get_PMs(names_only=True)

        self._project_form_view.set_GCs(GCs)
        self._project_form_view.set_PMs(PMs)
                
        self._project_form_view.set_callbacks({
            "edit_GCs_btn": self._edit_GCs_btn_click_handler,
            "edit_PMs_btn": self._edit_PMs_btn_click_handler,
            "create_btn": self._create_btn_click_handler,
            "cancel_btn": self._cancel_btn_click_handler
        })

    def __del__(self):
        print("deleting project form option")

    def _create_btn_click_handler(self):
        form_values = self._project_form_view.get_values()
        if self._project_form_model.validate(form_values):
            resp = self._project_form_model.create_project(form_values)
            if resp["success"]:
                self.events.emit({
                    "type": "new_project_created",
                    "data": resp["data"]
                })
                Modal.hide()
                Modal.clear()
            else:
                if resp["msg"] == "job_id conflict":
                    self._project_form_view.set_feedback_text("A project already exists with the given ID.")
                    self._project_form_view.highlight_input("job_id")
                elif resp["msg"] == "name conflict":
                    self._project_form_view.set_feedback_text("A project already exists with the given name.")
                    self._project_form_view.highlight_input("name")
                self._project_form_view.show_feedback()
        else:
            for key, value in form_values.items():
                if value == "":
                    self._project_form_view.highlight_input(key)

    def _edit_GCs_btn_click_handler(self):
        GCs_data = self._project_form_model.get_GCs()
        self._list_editor_view.set_data(GCs_data)
        self._list_editor_view.set_callbacks({
            "add_btn": "",
            "edit_btn": "",
            "delete_btn": "",
            "back_btn": ""
        })

    def add_GC_btn_click_handler(self):
        Modal.set_title("Add GC")
        Modal.clear()
        self._text_input_form_view.set_save_btn_callback()
        
    def edit_GC_btn_click_handler(self):
        Modal.set_title("Edit GC")
        self._text_input_form_view.set_save_btn_callback()
        Modal.clear()

    def delete_GC_btn_click_handler(self):
        Modal.set_title("Delete GC")
        self._text_input_form_view.set_save_btn_callback()
        Modal.clear()

    def _edit_PMs_btn_click_handler(self):
        PMs_data = self._project_form_model.get_PMs()
        self._list_editor_view.set_data(PMs_data)
        self._list_editor_view.set_callbacks({
            "add_btn": "",
            "edit_btn": "",
            "delete_btn": "",
            "back_btn": ""
        })

    def _cancel_btn_click_handler(self):
        Modal.hide()
        Modal.clear()

    def render(self):
        self._project_form_view.render()