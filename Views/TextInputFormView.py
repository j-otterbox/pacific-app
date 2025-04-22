import dearpygui.dearpygui as dpg
import constants as c
from Modules.Database import Database
from collections.abc import Callable

class TextInputFormView:
    def __init__(self):
        with dpg.stage() as self._stage_id:
            with dpg.group(horizontal=True):
                self._text_input_label = dpg.add_text()
                self._text_input = dpg.add_input_text(width=270)
            self._feedback_text = dpg.add_text(c.COLORS["red"], show=False)
            dpg.add_separator()
            with dpg.group(horizontal=True, indent=188):
                self._save_btn = dpg.add_button(label="Save", width=55)
                self._cancel_btn = dpg.add_button(label="Cancel", width=55)

    def get_value(self) -> str:
        return dpg.get_value(self._text_input)

    def set_value(self, value:str) -> None:
        dpg.set_value(self._text_input, value)

    def set_feedback(self, feedback:str) -> None:
        dpg.set_value(self._feedback_text, feedback)
        
    def show_feedback(self) -> None:
        dpg.show_item(self._feedback_text)
        
    def hide_feedback(self) -> None:
        dpg.hide_item(self._feedback_text)

    def set_save_btn_callback(self, callback:Callable) -> None:
        dpg.set_item_callback(self._save_btn, callback)

    def set_cancel_btn_callback(self, callback:Callable) -> None:
        dpg.set_item_callback(self._cancel_btn, callback)

    def clear(self) -> None:
        dpg.set_value(self._text_input , "")
        dpg.hide_item(self._feedback_text)

    def render(self, parent) -> None:
        """ Moves the item from staging to a child of the given parent. """
        self._parent = parent
        dpg.push_container_stack(parent)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()
        
