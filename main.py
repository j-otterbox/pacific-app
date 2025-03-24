
from Database import initialize_db
import dearpygui.dearpygui as dpg
from Views.Login import Login

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
        Login(primary_window)
    dpg.set_primary_window(primary_window, True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
