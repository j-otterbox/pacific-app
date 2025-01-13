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
                            dpg.add_menu_item(label="New Project", parent=menu_id, callback=self._new_project_btn_handler)
                        
                            # TODO: provide options to sort and filter + search
                        
                        with dpg.window(label="New Project", modal=True, show=False) as self._new_project_modal_id:
                            with dpg.group(horizontal=True, horizontal_spacing=15):
                                with dpg.group(horizontal=True):
                                    dpg.add_text("ID")
                                    dpg.add_input_text(decimal=True, width=60)
                                with dpg.group(horizontal=True):
                                    dpg.add_text("Name")
                                    dpg.add_input_text(width=227)
                            with dpg.group(horizontal=True, horizontal_spacing=25):
                                with dpg.group(horizontal=True):
                                    dpg.add_text("GC")
                                    dpg.add_combo(["", "Fairfield", "Holland", "W.E. O'Neil"], width=130)
                                    dpg.add_button(label="Manage GCs")
                                with dpg.group(horizontal=True):
                                    dpg.add_text("PM")
                                    dpg.add_combo(["", "Clint", "Lisa", "Michael", "Jermey", "Rob", "Rymmy"], width=75)

                            dpg.add_separator()

                            with dpg.group(horizontal=True, indent=251):
                                dpg.add_button(label="Create")
                                dpg.add_button(label="Cancel")

                            # label

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

                    

    def _new_project_btn_handler(self):
        dpg.show_item(self._new_project_modal_id)

    def _new_project_cancel_btn_handler(self):
        dpg.hide_item(self._new_project_modal_id)

    def render_view(self):
        dpg.move_item(self._dashboard_group_id, parent=self._primary_window)

