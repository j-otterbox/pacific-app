import dearpygui.dearpygui as dpg
from collections.abc import Callable

class ManagerFormView:
    def __init__(self):
        with dpg.stage() as self._stage_id:
            with dpg.group(horizontal=True):
                self._selectables_list = dpg.add_child_window(width=240, height=200)

                with dpg.child_window(border=False, height=200):
                    self._add_btn = dpg.add_button(label="Add", width=55)
                    self._edit_btn = dpg.add_button(label="Edit", enabled=False, width=55)
                    self._delete_btn = dpg.add_button(label="Delete", enabled=False, width=55)
                    self._back_btn = dpg.add_button(label="Back", width=55)

    def get_stage_id(self):
        return self._stage_id

    def set_add_btn_callback(self, callback:Callable):
        dpg.set_item_callback(self._add_btn, callback)

    def set_edit_btn_callback(self, callback:Callable):
        dpg.set_item_callback(self._edit_btn, callback)

    def set_delete_btn_callback(self, callback:Callable):
        dpg.set_item_callback(self._delete_btn, callback)

    def set_back_btn_callback(self, callback:Callable):
        dpg.set_item_callback(self._back_btn, callback)

    def set_selectables_list_data(self, data:list):
        for elem in data:
            dpg.add_selectable(
                parent=self._selectables_list,
                label=elem["name"],
                callback=self._selectable_click_handler,
                user_data=elem
            )

    def _selectable_click_handler(self, sender) -> None:
        """ Toggles selectable on/off, only one item toggled on max. """
        self._toggled_selectable = dpg.get_value(sender)
        
        if self._toggled_selectable:
            dpg.enable_item(self._edit_btn)
            dpg.enable_item(self._delete_btn)
        else:
            dpg.disable_item(self._edit_btn)
            dpg.disable_item(self._delete_btn)

        selectables = dpg.get_item_children(self._selectables_list)[1]
        for item in selectables:
            if item != sender:
                dpg.set_value(item, False)