import dearpygui.dearpygui as dpg
from collections.abc import Callable

class DashboardPageView():
    def __init__(self):
        with dpg.stage() as self._stage_id:
            with dpg.group(horizontal=True):
                with dpg.child_window(height=-1, width=325, menubar=True):
                    with dpg.menu_bar():
                        with dpg.menu(label="Project Explorer"):
                            self._new_project_menu_item = dpg.add_menu_item(label="New Project")
    
                    with dpg.child_window(border=False) as self._projects_list:
                        pass # projects from database go here

                with dpg.child_window(height=-1, menubar=True):
                    with dpg.menu_bar():
                        dpg.add_menu(label="What's going on...")

            # with dpg.window(width=322, autosize=True, min_size=[322, 80], modal=True, no_collapse=True, on_close=self.clear_modal, show=False) as self._modal:
            #     pass

    def set_new_project_menu_item_callback(self, callback:Callable):
        dpg.set_item_callback(self._new_project_menu_item, callback)

    def render(self, parent:int|str) -> None:
        dpg.set_viewport_width(700)
        dpg.set_viewport_height(400)
        dpg.push_container_stack(parent)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()