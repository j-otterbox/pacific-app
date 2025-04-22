from os.path import exists
import dearpygui.dearpygui as dpg
from dotenv import get_key
if not exists(get_key(".env", "DATABASE_NAME")):
    from Modules.Database import init_database
    init_database()
from Views.AppView import AppView
from Components.LoginPage import LoginPage
from Components.DashboardPage import DashboardPage
from Components.ProjectPage import ProjectPage

class App:
    def __init__(self):
        self._app_view = AppView()

        self._login_page = LoginPage()
        self._dashboard_page = DashboardPage()
        self._project_page = ProjectPage()
    
        self._login_page.events.subscribe("login_success", self._dashboard_page)
        self._dashboard_page.events.subscribe("new_project_created", self._project_page)
        self._project_page.events.subscribe("close_project", self._dashboard_page)

        self._app_view.render_primary_window()
        self._login_page.view.render()
        self._app_view.start_render_loop()