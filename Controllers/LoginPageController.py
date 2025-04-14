
from time import sleep
from Models.LoginPageModel import LoginPageModel
from Views.LoginPageView import LoginPageView
from Events.EventManager import EventManager
from util import clear_content_window

class LoginPageController:
    def __init__(self):
        self._model = LoginPageModel()
        self._view = LoginPageView()
        self.events = EventManager()

        self._view.set_submit_btn_callback(self._submit_btn_click_handler)

    def _submit_btn_click_handler(self):
        username = self._view.get_username()
        password = self._view.get_password()
        
        if self._model.validate_login(username, password) or True:
            clear_content_window()
            self._view.render_welcome_msg(username)
            sleep(1)
            clear_content_window()
            self.events.emit("login_success", {
                "event_type": "login_success",
                "username": username
            })
        else:
            self._view.show_invalid_login_msg()

    def render(self, parent:int|str):
        self._view.render(parent)

    def update(data:dict):
        pass