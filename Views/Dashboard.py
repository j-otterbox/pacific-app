import dearpygui.dearpygui as dpg

class Dashboard:
    def __init__(self):
        with dpg.stage() as self._staging_container_id:
            
            with dpg.table():
                dpg.add_table_column(label="Project", width_fixed=True)
                dpg.add_table_column(label="G.C.", width_fixed=True)
                dpg.add_table_column(label="Status")

                with dpg.table_row():
                    dpg.add_button(label="123 Main St.")
                    dpg.add_text("W.E. O'Neil")
                    dpg.add_text("3 Tasks Open, 10 Submittals Left")

                with dpg.table_row():
                    dpg.add_button(label="Glassell Park")
                    dpg.add_text("Fairfield")
                    dpg.add_text("2 Tasks Open, 5 Submittals Left")


    def render_view(self):
        dpg.unstage(self._staging_container_id)


dpg.create_context()
dpg.create_viewport(title='Pacific Carpets', width=800, height=600, resizable=False)

with dpg.window(tag="primary_window"):
    Dashboard().render_view()

dpg.set_primary_window("primary_window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
