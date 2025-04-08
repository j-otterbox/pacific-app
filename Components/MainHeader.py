import dearpygui.dearpygui as dpg

class MainHeader:
    def __init__(self, parent:int): 
        with dpg.table(parent=parent, header_row=False):
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