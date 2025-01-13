import dearpygui.dearpygui as dpg

class NewProjectForm:
    def __init__(self):
        with dpg.stage() as self._stage_id:
            with dpg.group(horizontal=True, horizontal_spacing=15):
                with dpg.group(horizontal=True):
                    dpg.add_text("ID")
                    dpg.add_input_text(decimal=True, width=60)
                with dpg.group(horizontal=True):
                    dpg.add_text("Name")
                    dpg.add_input_text(width=227)
            with dpg.group(horizontal=True, horizontal_spacing=25):
                with dpg.group(horizontal=True):
                    dpg.add_text("GC")
                    dpg.add_combo(["", "Fairfield", "Holland", "W.E. O'Neil"], width=130)
                    dpg.add_button(label="Manage GCs")
                with dpg.group(horizontal=True):
                    dpg.add_text("PM")
                    dpg.add_combo(["", "Clint", "Lisa", "Michael", "Jermey", "Rob", "Rymmy"], width=75)

            dpg.add_separator()

            with dpg.group(horizontal=True, indent=251):
                dpg.add_button(label="Create")
                dpg.add_button(label="Cancel")

    def render(self):
        dpg.unstage(self._stage_id)