import dearpygui.dearpygui as dpg

class BaseView:
    def __init__(self):
        self._primary_window = "primary_window"
        self._modal = "primary_modal"

    def _delete_primary_window_children(self):
        dpg.delete_item(item=self._primary_window, children_only=True)

    def _set_modal_title(self, title:str):
        dpg.configure_item(self._modal, label=title)
