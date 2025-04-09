from os import getenv
from Database import initialize_db
import dearpygui.dearpygui as dpg
from Components.MainHeader import MainHeader
from Views.LoginView import LoginForm
from Models.App import App

def register_textures():
    width, height, channels, data = dpg.load_image("Assets/pac_c_logo.png")
    with dpg.texture_registry():
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="pac_c_logo")

if __name__ == "__main__":
    initialize_db()
    dpg.create_context()
    register_textures()

    primary_window = App.primary_window.value
    content_window = App.content_window.value

    dpg.create_viewport(title="Pacific Carpets LLC", width=405, height=200, resizable=True)
    with dpg.window(tag=primary_window):
        MainHeader(parent=primary_window)
        dpg.add_child_window(tag=content_window, border=False)

    dpg.set_primary_window(primary_window, True)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
