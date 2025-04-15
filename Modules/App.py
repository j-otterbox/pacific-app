import dearpygui.dearpygui as dpg
import constants as c
from Controllers.LoginPageController import LoginPageController
from Controllers.DashboardPageController import DashboardPageController
from Controllers.ProjectPageController import ProjectPageController
from Components.MainHeader import MainHeader
from Modules.Database import init_database

class App:
    def __init__(self, title:str):
        dpg.create_context()
        dpg.create_viewport(title=title)
        self._register_textures()

        self._login_page = LoginPageController()
        self._dashboard_page = DashboardPageController()
        self._project_page = ProjectPageController()
    
        self._login_page.events.subscribe("login_success", self._dashboard_page)
        # self._dashboard_page.subscribe("logout", self._login_page)

    def _register_textures(self):
        width, height, channels, data = dpg.load_image("Assets/pac_c_logo.png")
        with dpg.texture_registry():
            dpg.add_static_texture(width=width, height=height, default_value=data, tag=c.PAC_LOGO)

    def init_database(self) -> None:
        init_database()

    def render_primary_window(self) -> None:
        """ Creates the base template for the app which consists of a header and body. """        
        with dpg.window(tag=c.PRIMARY_WINDOW):
            MainHeader(parent=c.PRIMARY_WINDOW)
            dpg.add_child_window(tag=c.CONTENT_WINDOW, border=False)
            dpg.add_window(tag=c.MODAL, modal=True, show=False)
        dpg.set_primary_window(c.PRIMARY_WINDOW, True)

    def render_login(self) -> None:
        self._login_page.render(c.CONTENT_WINDOW)

    def start_render_loop(self) -> None:
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()