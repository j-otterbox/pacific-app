from hashlib import sha256
from time import sleep
from Database import Database
from Views.LoginView import LoginView
from Events.EventManager import EventManager


class LoginController:
    def __init__(self):
        self.events = EventManager()
        self.view = LoginView()
        self.view.set_submit_btn_callback(self._submit_btn_click_handler)
        self.view.set_exit_btn_callback(self._exit_btn_click_handler)

    def _submit_btn_click_handler(self):
        username = self.view.get_username()
        password = self.view.get_password()
        password_hash_str = self._convert_to_hash_str(password)

        if self._is_valid_login(username, password_hash_str) or True:
            self.events.emit("on_login", {})

    def _exit_btn_click_handler(self):
        print("app exit detected")

    def _is_valid_login(self, username:str, password_hash_str:str) -> bool:
        db = Database()
        user = db.get_user_by_username(username)
        if user is not None:
            return user["pass_hash"] == password_hash_str
        return False

    def _convert_to_hash_str(self, password:str) -> str:
        bytes = bytearray(password, encoding="utf8")
        hash_obj = sha256(bytes)
        pass_hash_str = hash_obj.hexdigest()
        return pass_hash_str

    def update(data:dict):
        pass

    # def _submit(self):
    #     username = dpg.get_value(self._username_input)
    #     password = dpg.get_value(self._password_input)
    #     password_hash_str = convert_to_hash_str(password)

    #     if is_valid_login(username, password_hash_str) or True:
    #         self.events.emit("on_login")
    #         dpg.delete_item(self._parent, children_only=True)
    #         welcome_msg = dpg.add_text(f"Welcome, {username}.", parent=self._parent)
    #         dpg.set_item_pos(welcome_msg, [135, 40])
    #         sleep(1)
    #         dpg.delete_item(welcome_msg)
    #         DashboardView().unstage(self._parent)
    #     else:
    #         dpg.set_value(self._feedback_text_id, "username and password combination incorrect.")
    #         dpg.show_item(self._feedback_text_row_id)

