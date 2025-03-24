import dearpygui.dearpygui as dpg
from hashlib import sha256
from time import sleep
from .Dashboard import Dashboard
from Database import Database

# TODO: add logging to this action

class Login():
    def __init__(self, parent:int|str):
        self._parent = parent

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

        # content
        with dpg.table(header_row=False):
            dpg.add_table_column(width_fixed=True)
            dpg.add_table_column()

            with dpg.table_row(): 
                dpg.add_text("Username")
                self._username_input = dpg.add_input_text(width=-1)
            with dpg.table_row(): #
                dpg.add_text("Password")
                self._password_input = dpg.add_input_text(password=True, width=-1)
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
        username = dpg.get_value(self._username_input)
        password = dpg.get_value(self._password_input)
        bytes = bytearray(password, encoding="utf8")
        hash_obj = sha256(bytes)
        pass_hash_str = hash_obj.hexdigest()

        if self._is_valid_login(username, pass_hash_str):
            dpg.delete_item(self._parent, children_only=True)
            welcome_msg_id = dpg.add_text(f"Welcome, {username}.", parent=self._parent)
            dpg.set_item_pos(welcome_msg_id, [135, 95])
            sleep(1)
            dpg.delete_item(welcome_msg_id)
            dpg.set_viewport_width(600)
            dpg.set_viewport_height(400)
            Dashboard(self._parent)
        else:
            dpg.set_value(self._feedback_text_id, "username and password combination incorrect.")
            dpg.show_item(self._feedback_text_row_id)

    def _is_valid_login(self, username:str, password_hash_str:str):
        db = Database()
        user = db.get_user_by_username(username)
        if user is not None:
            return user["pass_hash"] == password_hash_str
        return False

    def _exit(self):
        dpg.destroy_context()


