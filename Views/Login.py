import dearpygui.dearpygui as dpg
from hashlib import sha256
from time import sleep
from dotenv import dotenv_values
from .Dashboard import Dashboard

# TODO: add logging to this action

class Login():
    def __init__(self, parent:int|str):
        self.__parent = parent
        self.__config = dotenv_values(".env")

        with dpg.table(header_row=False):
            dpg.add_table_column()
            dpg.add_table_column(width_fixed=True)
            dpg.add_table_column()

            with dpg.table_row():
                with dpg.table_cell():
                    pass
                with dpg.table_cell():
                    dpg.add_image("pac_c_logo")
                with dpg.table_cell():
                    pass

        with dpg.table(header_row=False):
            dpg.add_table_column(width_fixed=True)
            dpg.add_table_column()

            with dpg.table_row(): 
                dpg.add_text("Username")
                self._username_input_id = dpg.add_input_text(width=-1)
            with dpg.table_row(): #
                dpg.add_text("Password")
                self._password_input_id = dpg.add_input_text(password=True, width=-1)
            with dpg.table_row(show=False) as self._feedback_text_row_id: 
                with dpg.table_cell():
                    pass
                with dpg.table_cell():
                    self._feedback_text_id = dpg.add_text()
            with dpg.table_row(): 
                with dpg.table_cell():
                    pass
                with dpg.table_cell():
                    with dpg.group(horizontal=True):
                        dpg.add_text(indent=206)
                        dpg.add_button(label="Submit", callback=self._submit)
                        dpg.add_button(label="Exit", callback=self._exit)

    def _submit(self):
        username = dpg.get_value(self._username_input_id)
        password = dpg.get_value(self._password_input_id)

        bytes = bytearray(password, encoding="utf8")
        password_hash = sha256(bytes)
        password_hash_str = password_hash.hexdigest()

        if self._verify_login(username, password_hash_str) or True: # use during development only
            dpg.delete_item(self.__parent, children_only=True)
            welcome_msg_id = dpg.add_text(f"Welcome, {username}.", parent=self.__parent)
            dpg.set_item_pos(welcome_msg_id, [135, 95])
            sleep(1)
            dpg.delete_item(welcome_msg_id)
            dpg.set_viewport_width(600)
            dpg.set_viewport_height(400)
            Dashboard(self.__parent)

        else:
            dpg.set_value(self._feedback_text_id, "username and password combination incorrect.")
            dpg.show_item(self._feedback_text_row_id)

    def _verify_login(self, username:str, password_hash_str:str):
        user_match = username == self.__config.get("USERNAME")
        password_hash_match = password_hash_str == self.__config.get("PASS_HASH")
        return user_match and password_hash_match

    def _exit(self):
        dpg.destroy_context()


