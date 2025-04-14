import dearpygui.dearpygui as dpg
from Views.ProjectFormView import ProjectFormView
from collections.abc import Callable

class DashboardPageView():
    def __init__(self):
        self._project_form = ProjectFormView()

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

            with dpg.window(width=322, autosize=True, min_size=[322, 80], modal=True, no_collapse=True, on_close=self.clear_modal, show=False) as self._modal:
                pass
        
    def get_project_form(self):
        return self._project_form

    def get_modal(self) -> int:
        """ Returns the id of the dashboard modal. """
        return self._modal

    def set_modal_label(self, label:str):
        dpg.set_item_label(self._modal, label)

    def show_modal(self):
        dpg.show_item(self._modal)
        
    def set_new_project_menu_item_callback(self, callback:Callable):
        dpg.set_item_callback(self._new_project_menu_item, callback)

    def hide_modal(self):
        dpg.hide_item(self._modal)

    def _new_project_btn_handler(self):
        self.set_modal_label("Create New Project")
        self._project_form.render()
        self._project_form.clear()
        dpg.show_item(self._modal)

    def clear_modal(self):
        dpg.delete_item(self._modal, children_only=True)

    def render(self, parent:int|str) -> None:
        dpg.set_viewport_width(700)
        dpg.set_viewport_height(400)
        dpg.push_container_stack(parent)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()