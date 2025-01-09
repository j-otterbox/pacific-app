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

                    with dpg.collapsing_header(label="GC - Project Name"):
                        with dpg.group(horizontal=True):
                            dpg.add_button(label="Open", small=True)
                            dpg.add_button(label="Delete", small=True)
                            with dpg.popup(dpg.last_item(), modal=True, mousebutton=dpg.mvMouseButton_Left):
                                dpg.add_text("Please confirm you want to delete project [PROJECT NAME].")
                                with dpg.group(horizontal=True, indent=144):
                                    dpg.add_button(label="Yes", width=50)
                                    dpg.add_button(label="No", width=50)
                                # dpg.add_separator()
                                # dpg.add_checkbox(label="Don't ask me next time")
                        dpg.add_separator()
                        dpg.add_text("Samples")
                        dpg.add_progress_bar(label="Progress Bar", width=-1, default_value=1, overlay="100% Ordered from Vendors")
                        dpg.add_progress_bar(label="Progress Bar", width=-1, default_value=0.78, overlay="78% Delivered to PC")
                        dpg.add_progress_bar(label="Progress Bar", width=-1, default_value=0.78, overlay="78% Shipped to GC")
                        dpg.add_progress_bar(label="Progress Bar", width=-1, default_value=0.56, overlay="56% Approved by GC")

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
