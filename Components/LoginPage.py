
from time import sleep
import constants as c
from Models.LoginPageModel import LoginPageModel
from Views.LoginPageView import LoginPageView
from Modules.EventManager import EventManager
from Modules.GuiManager import ContentWindow

class LoginPage:
    def __init__(self):
        self._model = LoginPageModel()
        self.view = LoginPageView()
        self.events = EventManager()

        self.view.set_submit_btn_callback(self._submit_btn_click_handler)

    def _submit_btn_click_handler(self):
        username = self.view.get_username()
        password = self.view.get_password()
        
        if self._model.validate_login(username, password) or True:
            ContentWindow.clear()
            self.view.render_welcome_msg(username)
            sleep(1)
            ContentWindow.clear()
            self.events.emit({
                "type": "login_success",
                "data": {
                    "username": username
                }  
            })
        else:
            self.view.show_invalid_login_msg()

    def update(data:dict):
        pass