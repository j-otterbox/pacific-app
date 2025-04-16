import dearpygui.dearpygui as dpg
from collections.abc import Callable

class ProjectPageView:
    def __init__(self):
        with dpg.stage() as self._stage_id:
            dpg.add_text("I am the project page")
            with dpg.group(horizontal=True):
                self._logout_btn = dpg.add_button(label="Logout")
                self._dashboard_btn = dpg.add_button(label="Dashboard")

    def set_logout_btn_callback(self, callback:Callable) -> None:
        dpg.set_item_callback(self._logout_btn, callback)

    def set_dashboard_btn_callback(self, callback:Callable) -> None:
        dpg.set_item_callback(self._dashboard_btn, callback)

    def render(self, parent:int|str):
        dpg.push_container_stack(parent)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()