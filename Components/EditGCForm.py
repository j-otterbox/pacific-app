import dearpygui.dearpygui as dpg

class EditGCForm:
    def __init__(self):
        with dpg.stage() as self._stage_id:
            with dpg.group(horizontal=True):
                dpg.add_text("Name")
                self._text_input = dpg.add_input_text(width=270)
            self._form_feedback = dpg.add_text(color=(220,53,69), show=False)
            dpg.add_separator()
            with dpg.group(horizontal=True, indent=188):
                self._submit_btn= dpg.add_button(label="Save", callback=self._submit_btn_handler, width=55)
                dpg.add_button(label="Back", callback=self._back_btn_handler, width=55)

    def _submit_btn_handler(self):
        pass

    def _back_btn_handler(self):
        pass

    def render(self):
        pass
