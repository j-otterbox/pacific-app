import dearpygui.dearpygui as dpg
from Components.NewProjectModal import NewProjectModal
    
# for testing
    # project_status = {
    #     "name": "8th & Alameda",
    #     "gc": "AECOM",
    #     "ordered": 0.75,
    #     "received": 0.65,
    #     "shipped": 0.23,
    #     "approved": 0.1,
    #     "data_gathered": 0.55,
    # }

    # ProjectExplorerListItem(item_data=project_status).render()

class Dashboard():
    def __init__(self):
        with dpg.stage():
            with dpg.group() as self._dashboard_group_id:
                with dpg.table(header_row=False):
                    dpg.add_table_column()
                    dpg.add_table_column(width_fixed=True)
                    dpg.add_table_column()

                    with dpg.table_row():
                        with dpg.table_cell():
                            pass
                        with dpg.table_cell():
                            dpg.add_image("pac_c_logo")
                        with dpg.table_cell():
                            pass

                with dpg.group(horizontal=True) as project_explorer_container_id:
                    with dpg.child_window(height=400, width=325, menubar=True):
                        with dpg.menu_bar():
                            menu_id = dpg.add_menu(label="Project Explorer")
                            self.__new_project_btn = dpg.add_menu_item(label="New Project", parent=menu_id)
                        
                            # TODO: provide options to sort and filter + search
                            # label

                        self.__projects_list = dpg.add_group()

                    with dpg.child_window(height=400, menubar=True):
                        with dpg.menu_bar():
                            dpg.add_menu(label="What's going on...")

                    self.__new_project_modal = NewProjectModal(self.__projects_list)
                    dpg.set_item_callback(self.__new_project_btn, self.__new_project_modal.show)

    def render_view(self):
        dpg.move_item(self._dashboard_group_id, parent="primary_window")

