import dearpygui.dearpygui as dpg
from Controllers.LoginPageController import LoginPageController
from Controllers.DashboardPageController import DashboardPageController
from Controllers.ProjectPageController import ProjectPageController
from Components.MainHeader import MainHeader
from util import named_items

class App:
    def __init__(self):
        self._login_page = LoginPageController()
        self._dashboard_page = DashboardPageController()
        self._project_page = ProjectPageController()

        self._login_page.events.subscribe("login_success", self._dashboard_page)
        # self._dashboard_page.subscribe("logout", self._login_page)

    def render_primary_window(self):
        primary_window = named_items.primary_window.value
        content_window = named_items.content_window.value

        self._register_textures()

        with dpg.window(tag=primary_window):
            MainHeader(parent=primary_window)
            dpg.add_child_window(tag=content_window, border=False)
            dpg.add_window(tag=named_items.modal, modal=True, show=False)
        dpg.set_primary_window(primary_window, True)
        
    def render_login_page(self):
        self._login_page.render(named_items.content_window.value)

    def _register_textures(self):
        width, height, channels, data = dpg.load_image("Assets/pac_c_logo.png")
        with dpg.texture_registry():
            dpg.add_static_texture(width=width, height=height, default_value=data, tag="pac_c_logo")