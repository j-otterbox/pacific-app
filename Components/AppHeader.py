import dearpygui.dearpygui as dpg
from Util import named_items

class AppHeader:
    def __init__(self):
        with dpg.stage() as self._stage_id:
            with dpg.table(header_row=False):
                dpg.add_table_column()
                dpg.add_table_column(width_fixed=True)
                dpg.add_table_column()

                with dpg.table_row():
                    with dpg.table_cell():
                        pass
                    with dpg.table_cell():
                        dpg.add_image(named_items.pacsee_logo.value)
                    with dpg.table_cell():
                        pass

    def render(self, parent:str):
        dpg.push_container_stack(parent)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()