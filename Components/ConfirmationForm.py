import dearpygui.dearpygui as dpg

class ConfirmationForm:
    def __init__(self):
        with dpg.stage() as self._stage_id:
            pass

    def render(self, parent):
        self._parent = parent
        dpg.push_container_stack(self._parent)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()
