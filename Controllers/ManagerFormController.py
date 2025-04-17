from Models.ManagerFormModel import ManagerFormModel
from Views.ManagerFormView import ManagerFormView
from Modules.EventManager import EventManager

class ManagerFormController:
    def __init__(self, PMs:bool=False, GCs:bool=False):
        self._model = ManagerFormModel()
        self._view = ManagerFormView()
        self.events = EventManager()

        if PMs:
            PM_data = self._model.get_PMs()
            self._view.set_selectables_list_data(PM_data)
            self._view.set_add_btn_callback()
            self._view.set_edit_btn_callback()
            self._view.set_delete_btn_callback()
        elif GCs:
            GC_data = self._model.get_GCs()
            self._view.set_selectables_list_data(GC_data)
            self._view.set_add_btn_callback()
            self._view.set_edit_btn_callback()
            self._view.set_delete_btn_callback()

        self._view.set_back_btn_callback()

    def _back_btn_callback(self):
        pass
    