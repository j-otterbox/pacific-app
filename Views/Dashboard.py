import dearpygui.dearpygui as dpg
from Components.ProjectForm import ProjectForm
    
class Dashboard():
    def __init__(self):
        dpg.set_viewport_width(600)
        dpg.set_viewport_height(400)
        self._project_form = ProjectForm()

        with dpg.stage() as self._stage_id:
            with dpg.group(horizontal=True):
                with dpg.child_window(height=400, width=325, menubar=True):
                    with dpg.menu_bar():
                        with dpg.menu(label="Project Explorer"):
                            dpg.add_menu_item(label="New Project", callback=self._create_project_btn_handler)

                        # menu_id = dpg.add_menu(label="Project Explorer")
                        # dpg.add_menu_item(label="New Project", parent=menu_id, callback=self._create_project_btn_handler)
                    
                    with dpg.child_window(border=False) as self._projects_list:
                        pass # will load existing projects

                with dpg.child_window(height=400, menubar=True):
                    with dpg.menu_bar():
                        dpg.add_menu(label="What's going on...")

            with dpg.window(width=322, autosize=True, min_size=[322, 80], modal=True, no_collapse=True, on_close=self._clear_modal, show=False) as self._modal:
                pass
            
    def _clear_modal(self):
        dpg.delete_item(self._modal, children_only=True)

    def _create_project_btn_handler(self):
        dpg.set_item_label(self._modal, "Create New Project")
        self._project_form.render(self._modal)
        self._project_form.clear()
        dpg.show_item(self._modal)

    def render(self, parent:int|str) -> None:
        """ Unstages the component as a child of the parent item. """
        dpg.push_container_stack(parent)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()