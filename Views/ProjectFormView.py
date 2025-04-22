
from collections.abc import Callable
import dearpygui.dearpygui as dpg
import constants as c

class ProjectFormView:
    def __init__(self):
        with dpg.stage() as self._stage_id:
            with dpg.group(horizontal=True):
                self._job_ID_input_label = dpg.add_text("Job ID")
                self._job_ID_text_input = dpg.add_input_text(decimal=True, width=55)

            with dpg.group(horizontal=True):
                self._GC_combo_label = dpg.add_text("GC", indent=28)
                self._GC_combo = dpg.add_combo(default_value="", width=184)
                self._edit_GCs_btn = dpg.add_button(label="Manage GCs")

            with dpg.group(horizontal=True):
                self._PM_combo_label = dpg.add_text("PM", indent=28)
                self._PM_combo = dpg.add_combo(default_value="", width=184)
                self._edit_PMs_btn = dpg.add_button(label="Manage PMs")

            with dpg.group(horizontal=True):
                self._name_input_label = dpg.add_text("Name", indent=14)
                self._name_text_input = dpg.add_input_text(width=-1)

            self._feedback_text = dpg.add_text(
                "Please make sure all fields are entered.",
                color=c.COLORS["red"],
                show=False
            )
            dpg.add_separator()
            
            with dpg.group(horizontal=True, indent=198):
                self._create_btn = dpg.add_button(label="Create")
                self._cancel_btn = dpg.add_button(label="Cancel")

    def get_values(self) -> dict[str]:
        return {
            "job_id": dpg.get_value(self._job_ID_text_input),
            "pm": dpg.get_value(self._PM_combo),
            "gc": dpg.get_value(self._GC_combo),
            "name": dpg.get_value(self._name_text_input)
        }

    def set_callbacks(self, callbacks:dict[str:Callable]) -> None:
        dpg.set_item_callback(self._edit_GCs_btn, callbacks["edit_GCs_btn"])
        dpg.set_item_callback(self._edit_PMs_btn, callbacks["edit_PMs_btn"])
        dpg.set_item_callback(self._create_btn, callbacks["create_btn"])
        dpg.set_item_callback(self._cancel_btn, callbacks["cancel_btn"])

    def set_GC_combo_items(self, items:list) -> None:
        dpg.configure_item(self._GC_combo, items=items)

    def set_PM_combo_items(self, items:list) -> None:
        dpg.configure_item(self._PM_combo, items=items)

    def set_feedback_text(self, text:str):
        dpg.set_value(self._feedback_text, text)

    def show_feedback(self):
        dpg.show_item(self._feedback_text)

    def highlight_input(self, name:str):
        label = ""
        match(name):
            case "job_id": label = self._job_ID_input_label
            case "pm":     label = self._PM_combo_label
            case "gc":     label = self._GC_combo_label
            case "name":   label = self._name_input_label
        dpg.configure_item(label, color=c.COLORS["red"])

    def clear(self) -> None:
        """ Sets the form back to its default state. """
        form_items = self._get_form_items()
        for label, input in form_items:
            dpg.configure_item(label, color=c.COLORS["white"])
            dpg.set_value(input, "")
        dpg.hide_item(self._feedback_text)

    def _get_form_items(self):
        return [
            (self._job_ID_input_label, self._job_ID_text_input),
            (self._PM_combo_label, self._PM_combo),
            (self._GC_combo_label, self._GC_combo),
            (self._name_input_label, self._name_text_input)
        ]

    def render(self, parent:int|str) -> None:
        dpg.push_container_stack(parent)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()
    
    # def __render_gcm(self):
    #     x = int((dpg.get_viewport_width()/2) - (self.__width/2))
    #     y = int((dpg.get_viewport_height()/2) - (235/2))

    #     dpg.set_item_pos(self.__id, [x,y])
 
    # def show(self):
    #     x = int((dpg.get_viewport_width()/2) - (self.__width/2))
    #     y = int((dpg.get_viewport_height()/2) - (self.__height/2))

    #     dpg.set_item_pos(self.__id, [x, y])
    #     dpg.show_item(self.__id)
