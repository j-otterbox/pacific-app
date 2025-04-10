from Controllers.LoginController import LoginController
from Controllers.DashboardController import DashboardController
from Util import named_items
from Views.AppView import AppView

class AppController:
    def __init__(self):
        self._view = AppView()
        self._login = LoginController()
        self._dashboard = DashboardController()
        self._login.events.subscribe("on_login", self._dashboard)
        self._dashboard.events.subscribe("on_logout", self._login)

    def bootstrap(self):
        """ Handles the startup process required by the GUI library and begins app execution. """
        content_window = named_items.content_window.value
        self._view.init_app_window()
        self._login.view.render(parent=content_window)
        self._view.start_render_loop()  


