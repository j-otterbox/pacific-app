import dearpygui.dearpygui as dpg
from hashlib import sha256
from time import sleep
from Database import Database
from Models.App import App
from Views.DashboardView import Dashboard

class LoginView():
    def __init__(self):
        with dpg.stage() as self._stage_id:
            with dpg.table(header_row=False):
                dpg.add_table_column(width_fixed=True)
                dpg.add_table_column()

                with dpg.table_row(): 
                    dpg.add_text("Username")
                    self._username_input = dpg.add_input_text(width=-1)
                with dpg.table_row(): 
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
                            dpg.add_button(label="Submit", callback=self._submit_btn_click_handler)
                            dpg.add_button(label="Exit", callback=self._exit_btn_click_handler)

    def _submit_btn_click_handler(self):
        username = dpg.get_value(self._username_input)
        password = dpg.get_value(self._password_input)
        bytes = bytearray(password, encoding="utf8")
        hash_obj = sha256(bytes)
        pass_hash_str = hash_obj.hexdigest()

        if self._is_valid_login(username, pass_hash_str) or True:
            content_container_tag = App.content_container.value
            dpg.delete_item(content_container_tag, children_only=True)
            welcome_msg = dpg.add_text(f"Welcome, {username}.", parent=content_container_tag)
            dpg.set_item_pos(welcome_msg, [135, 40])
            sleep(1)
            dpg.delete_item(welcome_msg)
            Dashboard()
        else:
            dpg.set_value(self._feedback_text_id, "username and password combination incorrect.")
            dpg.show_item(self._feedback_text_row_id)

    def _is_valid_login(self, username:str, password_hash_str:str):
        """ 
            Compares the given hash string against the user's hash string in the database.
        """
        db = Database()
        user = db.get_user_by_username(username)
        if user is not None:
            return user["pass_hash"] == password_hash_str
        return False

    def _exit_btn_click_handler(self) -> None:
        """ Destroys the current context, quitting the app. """
        dpg.destroy_context()

    def render(self) -> None:
        """ Unstages the Login View from wherever this method is called. """
        content_container_tag = App.content_container.value
        dpg.set_viewport_width(405)
        dpg.set_viewport_height(200)
        dpg.set_viewport_resizable(False)
        dpg.push_container_stack(content_container_tag)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()

