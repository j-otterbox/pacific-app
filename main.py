
import dearpygui.dearpygui as dpg
from Views.Login import Login
from Database import initialize_db

def load_assets():
    width, height, channels, data = dpg.load_image("Assets/pac_c_logo.png")
    with dpg.texture_registry():
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="pac_c_logo")

if __name__ == "__main__":
    initialize_db()
    dpg.create_context()
    load_assets()
    dpg.create_viewport(title='Pacific Carpets', width=405, height=200, resizable=False)
    with dpg.window() as primary_window:
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

        with dpg.child_window(border=False) as content_window: 
            Login().render(content_window)

    dpg.set_primary_window(primary_window, True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
