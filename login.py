import dearpygui.dearpygui as dpg

class Login:
    def __init__(self):
        with dpg.stage() as self._staging_contrainer_id:

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

            with dpg.table(header_row=False):
                dpg.add_table_column(width_fixed=True)
                dpg.add_table_column()

                with dpg.table_row(): 
                    dpg.add_text("Username")
                    dpg.add_input_text(width=-1)
                with dpg.table_row(): #
                    dpg.add_text("Password")
                    dpg.add_input_text(password=True, width=-1)
                with dpg.table_row(show=False): 
                    with dpg.table_cell():
                        pass
                    with dpg.table_cell():
                        dpg.add_text("login feedback here")
                with dpg.table_row(): 
                    with dpg.table_cell():
                        pass
                    with dpg.table_cell():
                        with dpg.group(horizontal=True):
                            dpg.add_text(indent=161)
                            dpg.add_button(label="Submit", callback=self._submit)
                            dpg.add_button(label="Exit", callback=self._exit)

    def _submit(self):
        print("submit button pressed")

    def _exit(self):
        print("exit button pressed")


dpg.create_context()
dpg.create_viewport(title='Pacific Carpets', width=360, height=200)

width, height, channels, data = dpg.load_image("Assets/pac_c_logo.png")

with dpg.texture_registry():
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="pac_c_logo")

with dpg.window(tag="primary_window"):
    login_window = Login()
    dpg.unstage(login_window._staging_contrainer_id)

dpg.set_primary_window("primary_window", True)
dpg.setup_dearpygui()
# dpg.show_item_registry()
# dpg.show_style_editor()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
