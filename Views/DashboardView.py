import dearpygui.dearpygui as dpg
from Components.ProjectForm import ProjectForm
from Models.App import App
from Util import set_modal_label, show_modal
    
class Dashboard():
    def __init__(self):
        with dpg.group(horizontal=True):
            with dpg.child_window(height=-1, width=325, menubar=True):
                with dpg.menu_bar():
                    with dpg.menu(label="Project Explorer"):
                        dpg.add_menu_item(label="New Project", callback=self._new_project_btn_click_handler)

                    # menu_id = dpg.add_menu(label="Project Explorer")
                    # dpg.add_menu_item(label="New Project", parent=menu_id, callback=self._new_project_btn_click_handler)
                projects_list = App.projects_list.value
                dpg.add_child_window(tag=projects_list, border=False)

            with dpg.child_window(height=-1, menubar=True):
                with dpg.menu_bar():
                    dpg.add_menu(label="What's going on...")

        modal_tag = App.modal.value
        self._modal = dpg.add_window(
            width=322,
            autosize=True,
            min_size=[322, 80],
            modal=True, no_collapse=True,
            on_close=self._clear_modal,
            show=False,
            tag=modal_tag
        )

    def _new_project_btn_click_handler(self):
        set_modal_label("Create New Project")
        self._project_form.render()
        show_modal()

    def _clear_modal(self):
        dpg.delete_item(self._modal, children_only=True)

    def render(self) -> None:
        content_container = App.content_container.value
        dpg.set_viewport_width(600)
        dpg.set_viewport_height(400)
        dpg.push_container_stack(content_container)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()