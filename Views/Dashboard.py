import dearpygui.dearpygui as dpg

def load_assets():
    width, height, channels, data = dpg.load_image("Assets/pac_c_logo.png")

    with dpg.texture_registry():
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="pac_c_logo")

class Dashboard:
    def __init__(self):
        with dpg.stage() as self._staging_container_id:
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

            with dpg.group(horizontal=True):
                with dpg.child_window(height=400, width=325, menubar=True):
                    with dpg.menu_bar():
                        dpg.add_menu(label="Project Explorer")
                        # provide options to sort and filter + search

                    # project list items go here...

                with dpg.child_window(height=400, menubar=True):
                    with dpg.menu_bar():
                        dpg.add_menu(label="What's going on...")

    def render_view(self):
        dpg.unstage(self._staging_container_id)


dpg.create_context()
dpg.create_viewport(title='Pacific Carpets', width=800, height=600, resizable=False)
load_assets()

with dpg.window(tag="primary_window"):
    Dashboard().render_view()

dpg.set_primary_window("primary_window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
