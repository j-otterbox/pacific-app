import dearpygui.dearpygui as dpg

# - basic database for samples 
# - TODO: needs CRUD functionality
# - CREATE (ui only)
# - READ
# - UPDATE
# - DELETE (ui only)

# - basic information about the samples is tracked (callout, vendor, style, etc.)
# - need to track: status, ETA if samples ordered, data gathered
# - later: transmittals should be able to be created from here
# - should be able to filter table, group by vendor,


def add_new_row(table_tag:int | str, spec_data:dict):
    with dpg.table_row(parent="spec_table"):

        for j in range(0, 9):
            if j == 0:
                dpg.add_text(f"{1}")
            elif j == 1: # row num
                dpg.add_checkbox()
            else:
                input_text_tag = dpg.add_input_text(width=-1)
                dpg.bind_item_handler_registry(input_text_tag, "table_cell_handler")

def delete_row(table_row_tag:int):
    row_tags = dpg.get_item_children("spec_table")[1]

    if row_tags:
        dpg.delete_item(row_tags[-1])

dpg.create_context()
dpg.create_viewport(title='Pacific Carpets', width=1200, height=800)

with dpg.window(tag="primary_window"):

    with dpg.group(horizontal=True):
        dpg.add_button(label="New Row", callback=add_new_row)
        dpg.add_button(label="Delete Row", callback=delete_row)

    with dpg.table(header_row=True, tag="spec_table") as table_tag:

        table_data = [
            {
                "callout": "T-01",
                "vendor": "Daltile",
                "style": "Lorem Ipsum",
                "color": "Beige",
                "finish": "Polished",
                "size": "12\"x48\"",
                "thickness": "8mm",
            },
            {
                "callout": "T-02",
                "vendor": "Stone Source",
                "style": "Lorem Ipsum",
                "color": "Gray",
                "finish": "Matte",
                "size": "8\"x8\"",
                "thickness": "10mm",
            },
            {
                "callout": "T-03",
                "vendor": "Emser",
                "style": "Lorem Ipsum",
                "color": "Absolute Black",
                "finish": "Honed",
                "size": "8\"X16\"",
                "thickness": "9mm",
            },
        ]

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

        def deactivated_handler():
            print("this cell has been deactivated")

        with dpg.item_handler_registry(tag="table_cell_handler"):
            dpg.add_item_deactivated_handler(callback=deactivated_handler)

        # creating a brand new table
    
        # if creating the table from existing data
        # for i in range(0, len(table_data)):
        #     with dpg.table_row() as row_tag:

        #         dpg.add_text(f"")

        #         for j in range(0, 9):
        #             if j == 0:
        #                 dpg.add_text(f"{i+1}")
        #             elif j == 1: # row num
        #                 dpg.add_checkbox()
        #             else:
        #                 input_text_tag = dpg.add_input_text(width=300)
        #                 dpg.bind_item_handler_registry(input_text_tag, "table_cell_handler")


def  log_key_press(e, c):
    print("arrow key was pressed")

with dpg.handler_registry():
    dpg.add_key_press_handler(key=dpg.mvKey_Right, callback=log_key_press)
    dpg.add_key_press_handler(key=dpg.mvKey_Down, callback=log_key_press)
    dpg.add_key_press_handler(key=dpg.mvKey_Left, callback=log_key_press)
    dpg.add_key_press_handler(key=dpg.mvKey_Up, callback=log_key_press)


dpg.set_primary_window("primary_window", True)

dpg.setup_dearpygui()
dpg.show_item_registry()
# dpg.show_style_editor()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()