import dearpygui.dearpygui as dpg
from Util import named_items
from Components.AppHeader import AppHeader
from Views.LoginView import LoginView

class AppView:
    def __init__(self):
        dpg.create_context()
        self._register_textures()

    def _register_textures(self):
        width, height, channels, data = dpg.load_image("Assets/pac_c_logo.png")
        with dpg.texture_registry():
            dpg.add_static_texture(width=width, height=height, default_value=data, tag="pac_c_logo")

    def init_app_window(self):
        """ Creates the viewport and basic app structure. """
        primary_window = named_items.primary_window.value
        content_window = named_items.content_window.value

        dpg.create_viewport(title="Pacific Carpets LLC")
        with dpg.window(tag=primary_window):
            AppHeader().render(parent=primary_window)
            dpg.add_child_window(tag=content_window, border=False)
        dpg.set_primary_window(primary_window, True)

    def start_render_loop(self):
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()












        




