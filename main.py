import dearpygui.dearpygui as dpg
from Models.App import App
from Components.MainHeader import MainHeader
from Views.LoginView import LoginView
from Database import initialize_db

def register_textures():
    width, height, channels, data = dpg.load_image("Assets/pac_c_logo.png")
    with dpg.texture_registry():
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="pac_c_logo")

if __name__ == "__main__":
    initialize_db()
    dpg.create_context()
    register_textures()

    primary_window = App.primary_window.value
    content_container = App.content_container.value

    dpg.create_viewport(title="Pacific Carpets LLC")
    with dpg.window(tag=primary_window):
        MainHeader(parent=primary_window)
        with dpg.child_window(tag=content_container, border=False):
            LoginView().render()
    dpg.set_primary_window(primary_window, True)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
