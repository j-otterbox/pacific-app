import dearpygui.dearpygui as dpg
import constants as c

class MainHeader:
    def __init__(self, parent:int|str):
        with dpg.table(parent=parent, header_row=False):
            dpg.add_table_column()
            dpg.add_table_column(width_fixed=True)
            dpg.add_table_column()

            with dpg.table_row():
                with dpg.table_cell():
                    pass
                with dpg.table_cell():
                    dpg.add_image(c.PAC_LOGO)
                with dpg.table_cell():
                        pass

