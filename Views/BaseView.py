import dearpygui.dearpygui as dpg

class BaseView:
    def __init__(self):
        self._primary_window = "primary_window"

    def _delete_primary_window_children(self):
        dpg.delete_item(item=self._primary_window, children_only=True)
