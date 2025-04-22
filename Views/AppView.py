import dearpygui.dearpygui as dpg
import constants as c
from PartialViews.MainHeader import MainHeader

class AppView:
    def __init__(self):
        dpg.create_context()
        self._register_textures()

        dpg.create_viewport(title="Pacific Carpets, LLC")
        with dpg.stage() as self._stage_id:
            with dpg.window(tag=c.PRIMARY_WINDOW):
                MainHeader(parent=c.PRIMARY_WINDOW)
                dpg.add_child_window(tag=c.CONTENT_WINDOW, border=False)
                dpg.add_window(
                    tag=c.MODAL,
                    modal=True,
                    autosize=True,
                    on_close=lambda:dpg.delete_item(c.MODAL, children_only=True),
                    show=False
                )
            dpg.set_primary_window(c.PRIMARY_WINDOW, True)
            dpg.show_item_registry()

    def _register_textures(self):
        width, height, channels, data = dpg.load_image("Assets/pac_c_logo.png")
        with dpg.texture_registry():
            dpg.add_static_texture(width=width, height=height, default_value=data, tag=c.PAC_LOGO)

    def render_primary_window(self) -> None:
        """ Creates the base template for all views throughout the app. """
        dpg.unstage(self._stage_id) # since there is no content, this automatically becomes the root
        dpg.delete_item(self._stage_id) # the staging area needs to be cleared manually (item registry is bugged?).

    def start_render_loop(self) -> None:
        """ This *must* happen last, after rendering of the primary window and login page. """
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
