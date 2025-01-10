import dearpygui.dearpygui as dpg

def load_assets(path:str):
    width, height, channels, data = dpg.load_image(f"{path}/pac_c_logo.png")

    with dpg.texture_registry():
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="pac_c_logo")

if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '')))
    from Components.ProjectExplorerListItem import ProjectExplorerListItem

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
                        project_explorer_menu_id = dpg.add_menu(label="Project Explorer")
                        dpg.add_menu_item(label="New Project", parent=project_explorer_menu_id, callback=self._new_project)
                    
                        # TODO: provide options to sort and filter + search

                    # for testing
                    # project_status = {
                    #     "name": "8th & Alameda",
                    #     "gc": "AECOM",
                    #     "ordered": 0.75,
                    #     "received": 0.65,
                    #     "shipped": 0.23,
                    #     "approved": 0.1,
                    #     "data_gathered": 0.55,
                    # }

                    # ProjectExplorerListItem(item_data=project_status).render()

                with dpg.child_window(height=400, menubar=True):
                    with dpg.menu_bar():
                        dpg.add_menu(label="What's going on...")

    def _new_project(self):
        print("I'm a new project.")

    def render_view(self):
        dpg.unstage(self._staging_container_id)

dpg.create_context()
dpg.create_viewport(title='Pacific Carpets', width=800, height=600, resizable=False)

if __name__ == "__main__": load_assets("../Assets")
else: load_assets("Assets")

with dpg.window(tag="primary_window"):
    Dashboard().render_view()

dpg.set_primary_window("primary_window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
