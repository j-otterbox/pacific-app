import dearpygui.dearpygui as dpg

# - basic database for samples 
# - needs CRUD functionality
# - basic information about the samples is tracked (callout, vendor, style, etc.)
# - need to track: status, ETA if samples ordered, data gathered
# - later: transmittals should be able to be created from here
# - should be able to filter table, group by vendor,

dpg.create_context()

with dpg.window(tag="primary_window"):
    with dpg.table(header_row=True):

        # table columns use child slot 0
        dpg.add_table_column(width_fixed=True)
        dpg.add_table_column(width_fixed=True)
        dpg.add_table_column(label="Callout")
        dpg.add_table_column(label="Vendor")
        dpg.add_table_column(label="Style")
        dpg.add_table_column(label="Color")
        dpg.add_table_column(label="Finish")
        dpg.add_table_column(label="Size")
        dpg.add_table_column(label="Thickness")

        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
        for i in range(0, 3):
            with dpg.table_row():
                for j in range(0, 8):
                    if j == 0: # row num
                        dpg.add_text(f"{i+1}")
                    elif j == 1:
                        dpg.add_checkbox()
                    else:
                        dpg.add_text(f"Row{i} Column{j}")
                        

dpg.create_viewport(title='Pacific Carpets', width=1200, height=800)
dpg.set_primary_window("primary_window", True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()