import dearpygui.dearpygui as dpg
from collections.abc import Callable

class ConfirmationForm:
    def __init__(self, confirm_btn_callback:Callable=None, cancel_btn_callback:Callable=None):
        with dpg.stage() as self._stage_id:
            self._prompt = dpg.add_text()
            with dpg.group(horizontal=True):
                self._confirm_btn = dpg.add_button(label="Yes")
                self._cancel_btn = dpg.add_button(label="No")

            if confirm_btn_callback is not None:
                dpg.set_item_callback(self._confirm_btn, confirm_btn_callback)
            if cancel_btn_callback is not None:
                dpg.set_item_callback(self._cancel_btn, cancel_btn_callback)
        
    def set_prompt(self, prompt:str) -> None:
        dpg.set_value(self._prompt, prompt)

    def set_confirm_callback(self, callback:Callable) -> None:
        dpg.set_item_callback(self._confirm_btn, callback)

    def set_cancel_callback(self, callback:Callable) -> None:
        dpg.set_item_callback(self._cancel_btn, callback)

    def render(self, parent):
        self._parent = parent
        dpg.push_container_stack(self._parent)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()
