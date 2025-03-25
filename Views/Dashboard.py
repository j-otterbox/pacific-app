import dearpygui.dearpygui as dpg
from Components.NewProjectModal import NewProjectModal
    
class Dashboard():
    def __init__(self):
        dpg.set_viewport_width(600)
        dpg.set_viewport_height(400)

        with dpg.stage() as self._stage_id:
            with dpg.group(horizontal=True):
                with dpg.child_window(height=400, width=325, menubar=True):
                    with dpg.menu_bar():
                        menu_id = dpg.add_menu(label="Project Explorer")
                        self.__new_project_btn = dpg.add_menu_item(label="New Project", parent=menu_id)
                    
                    with dpg.group() as self._projects_list:
                        pass

                with dpg.child_window(height=400, menubar=True):
                    with dpg.menu_bar():
                        dpg.add_menu(label="What's going on...")

                self.__new_project_modal = NewProjectModal(self._projects_list)
                dpg.set_item_callback(self.__new_project_btn, self.__new_project_modal.show)

    def render(self, parent):
        self._parent = parent
        dpg.push_container_stack(parent)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()