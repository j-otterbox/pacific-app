from hashlib import sha256
from time import sleep
from Database import Database
from Views.LoginView import LoginView
from Events.EventManager import EventManager
from Util import clear_content_window

class LoginController:
    def __init__(self):
        self.events = EventManager()
        self._view = LoginView()
        self._view.set_submit_btn_callback(self._submit_btn_click_handler)

    def _submit_btn_click_handler(self):
        username = self._view.get_username()
        password = self._view.get_password()
        password_hash_str = self._convert_to_hash_str(password)
        
        if self._is_valid_login(username, password_hash_str) or True:
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

    def _convert_to_hash_str(self, password:str) -> str:
        bytes = bytearray(password, encoding="utf8")
        hash_obj = sha256(bytes)
        pass_hash_str = hash_obj.hexdigest()
        return pass_hash_str

    def _is_valid_login(self, username:str, password_hash_str:str) -> bool:
        db = Database()
        user = db.get_user_by_username(username)
        if user is not None:
            return user["pass_hash"] == password_hash_str
        return False

    def render_view(self, parent:int|str):
        self._view.render(parent)

    def update(data:dict):
        pass


