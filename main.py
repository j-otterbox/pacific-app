from os import getenv
from Database import initialize_db
import dearpygui.dearpygui as dpg
from Components.MainHeader import MainHeader
from Components.LoginForm import LoginForm

def register_textures():
    width, height, channels, data = dpg.load_image("Assets/pac_c_logo.png")
    with dpg.texture_registry():
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="pac_c_logo")

if __name__ == "__main__":
    initialize_db()
    dpg.create_context()
    register_textures()

    dpg.create_viewport(title="Pacific Carpets LLC", width=405, height=200, resizable=True)
    PRIMARY_WINDOW = getenv("PRIMARY_WINDOW")
    with dpg.window(tag=PRIMARY_WINDOW):
        MainHeader(parent=PRIMARY_WINDOW)
        with dpg.child_window(border=False) as content_container:
            LoginForm().unstage(parent=content_container)
    dpg.set_primary_window(PRIMARY_WINDOW, True)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
