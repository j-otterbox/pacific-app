import dearpygui.dearpygui as dpg
from .BaseView import BaseView
    
class Dashboard(BaseView):
    def __init__(self):
        super().__init__()

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

                with dpg.group(horizontal=True):
                    with dpg.child_window(height=400, width=325, menubar=True) as project_explorer_window_id:
                        with dpg.menu_bar():
                            menu_id = dpg.add_menu(label="Project Explorer")
                            dpg.add_menu_item(label="New Project", parent=menu_id, callback=self._new_project)
                        
                            # TODO: provide options to sort and filter + search
                        
                        with dpg.window(label="Modal Title", height=100, width=200, modal=True, show=False) as self._new_project_modal_id:
                            pass

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

                    with dpg.child_window(height=400, menubar=True):
                        with dpg.menu_bar():
                            dpg.add_menu(label="What's going on...")

    def _new_project(self):
        dpg.show_item(self._new_project_modal_id)

    def render_view(self):
        dpg.move_item(self._dashboard_group_id, parent=self._primary_window)

