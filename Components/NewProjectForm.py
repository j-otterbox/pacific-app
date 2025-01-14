import dearpygui.dearpygui as dpg

class NewProjectForm:
    def __init__(self):
        with dpg.stage() as self._stage_id:
            with dpg.group(horizontal=True, horizontal_spacing=15):
                with dpg.group(horizontal=True):
                    dpg.add_text("ID")
                    self._id_input_id = dpg.add_input_text(decimal=True, width=60)
                with dpg.group(horizontal=True):
                    dpg.add_text("Name")
                    self._name_input_id = dpg.add_input_text(width=227)
            with dpg.group(horizontal=True, horizontal_spacing=25):
                with dpg.group(horizontal=True):
                    dpg.add_text("GC")
                    self._gc_combo_id = dpg.add_combo(["", "Fairfield", "Holland", "W.E. O'Neil"], width=130)
                    dpg.add_button(label="Manage GCs", callback=self._render_gc_manager)
                with dpg.group(horizontal=True):
                    dpg.add_text("PM")
                    self._pm_combo_id = dpg.add_combo(["", "Clint", "Lisa", "Michael", "Jermey", "Rob", "Rymmy"], width=75)

            dpg.add_text("Please make sure all fields have been entered.", show=False)

            dpg.add_separator()
            with dpg.group(horizontal=True, indent=251):
                self._submit_btn_id = dpg.add_button(label="Create")
                self._cancel_btn_id = dpg.add_button(label="Cancel", callback=self._cancel_btn_handler)

    def set_submit_callback(self, callback):
        dpg.configure_item(self._submit_btn_id, callback=callback)

    def _render_gc_manager(self):
        print("i open the gc manager")

    def _cancel_btn_handler(self):
        dpg.hide_item(self._parent)
        self.clear()
        
    def clear(self):
        dpg.set_value(self._id_input_id, "")
        dpg.set_value(self._name_input_id, "")
        dpg.set_value(self._gc_combo_id, "")
        dpg.set_value(self._pm_combo_id, "")

    def get_values(self):
        incomplete_fields = []
        values = {
            "id": dpg.get_value(self._id_input_id),
            "name": dpg.get_value(self._name_input_id),
            "gc": dpg.get_value(self._gc_combo_id),
            "pm": dpg.get_value(self._pm_combo_id)
        }

        for field, value in values.items():
            if not value:
                incomplete_fields.append(field)

        if not incomplete_fields:
            return values
        else: pass
            # self._show_feedback(incomplete_fields)

    def _show_feedback(self, incomplete_fields:list):
        with dpg.group():
            
            for field in incomplete_fields:
                dpg.add_text(field, bullet=True)

    def render(self, parent):
        self._parent=parent
        dpg.unstage(self._stage_id)