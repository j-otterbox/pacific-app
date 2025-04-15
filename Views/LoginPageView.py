import dearpygui.dearpygui as dpg
from collections.abc import Callable
import constants as c

class LoginPageView():
    def __init__(self):
        with dpg.stage() as self._stage_id:
            with dpg.table(header_row=False):
                dpg.add_table_column(width_fixed=True)
                dpg.add_table_column()

                with dpg.table_row(): 
                    dpg.add_text("Username")
                    self._username_text_input = dpg.add_input_text(width=-1)
                with dpg.table_row(): #
                    dpg.add_text("Password")
                    self._password_text_input = dpg.add_input_text(password=True, width=-1)
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
                            self._submit_btn = dpg.add_button(label="Submit")
                            self._exit_btn = dpg.add_button(label="Exit", callback=self._exit_btn_click_handler)

    def get_username(self) -> str:
        return dpg.get_value(self._username_text_input)

    def get_password(self) -> str:
        return dpg.get_value(self._password_text_input)

    def set_submit_btn_callback(self, callback:Callable) -> None:
        dpg.set_item_callback(self._submit_btn, callback)

    def _exit_btn_click_handler(self) -> None:
        dpg.destroy_context()

    def render_welcome_msg(self, username:str):
        welcome_msg = dpg.add_text(f"Welcome, {username}.", parent=c.CONTENT_WINDOW)
        dpg.set_item_pos(welcome_msg, [135, 40])

    def show_invalid_login_msg(self):
        dpg.set_value(self._feedback_text_id, "username and password combination incorrect.")
        dpg.show_item(self._feedback_text_row_id)

    def render(self, parent:int|str) -> None:
        dpg.set_viewport_width(405)
        dpg.set_viewport_height(200)
        dpg.set_viewport_resizable(False)   
        dpg.push_container_stack(parent)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()