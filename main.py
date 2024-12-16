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

# select  all  options
# all
# by vendor

def add_new_row(spec_data:dict):
    table_row_tags = dpg.get_item_children("spec_table")[1] # col 1  

    with dpg.table_row(parent="spec_table") as table_row_tag:

        for j in range(0, 9):
            if j == 0:
                dpg.add_text(f"{len(table_row_tags)+1}")
            elif j == 1: # row num
                dpg.add_checkbox()
            else:
                input_text_tag = dpg.add_input_text(width=-1)
                # dpg.bind_item_handler_registry(input_text_tag, "table_cell_handler")

    print(table_row_tags)

def delete_row(table_row_tag:int):
    row_tags = dpg.get_item_children("spec_table")[1]

    if row_tags:
        dpg.delete_item(row_tags[-1])

def get_row_checkbox_ids():
    table_rows = dpg.get_item_children("spec_table")[1]
    checkbox_ids = []

    for row in table_rows:
        checkbox_ids.append(dpg.get_item_children(row)[1][1])

    return checkbox_ids

def toggle_rows(item_id, item_value):
    caller_item_type = dpg.get_item_type(item_id)
    checkbox_ids = get_row_checkbox_ids()
    toggle_filter = None
    toggle_checkbox_value = None

    if caller_item_type == "mvAppItemType::mvCombo":
        toggle_checkbox_value = dpg.get_value("toggle_all_checkbox")
        toggle_filter = item_value
        
    elif caller_item_type == "mvAppItemType::mvCheckbox":
        toggle_checkbox_value = item_value
        toggle_filter = dpg.get_value("toggle_filter_combo")
                                      
    if toggle_filter == "None":
        if toggle_checkbox_value == True:
            dpg.set_value("toggle_all_checkbox", False)
            for id in checkbox_ids:
                dpg.set_value(id, False)

    elif toggle_filter == "All":

        if caller_item_type == "mvAppItemType::mvCheckbox":
            dpg.set_value("toggle_all_checkbox", toggle_checkbox_value)
            for id in checkbox_ids:
                dpg.set_value(id, toggle_checkbox_value)

        elif caller_item_type == "mvAppItemType::mvCombo":
            dpg.set_value("toggle_all_checkbox", True)
            for id in checkbox_ids:
                dpg.set_value(id, True)

# ==== BEGIN MAIN ====

dpg.create_context()
dpg.create_viewport(title='Pacific Carpets', width=1200, height=800)

with dpg.window(tag="primary_window"):
    with dpg.group(horizontal=True):
        with dpg.group(horizontal=True):
            dpg.add_checkbox(tag="toggle_all_checkbox", callback=toggle_rows)
            dpg.add_combo(tag="toggle_filter_combo", items=["None", "All"], callback=toggle_rows, default_value="None", fit_width=True)

        dpg.add_button(label="New Row", callback=add_new_row)
        dpg.add_button(label="Delete Row", callback=delete_row)

    with dpg.table(header_row=True, tag="spec_table") as table_tag:

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

        # def deactivated_handler(tag):
        #     print(f"cell {tag} has been deactivated")

        # with dpg.item_handler_registry(tag="table_cell_handler"):
        #     dpg.add_item_deactivated_handler(callback=deactivated_handler)

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
    print(dpg.get_active_window())

with dpg.handler_registry():
    dpg.add_key_press_handler(key=dpg.mvKey_Right, callback=log_key_press)
    dpg.add_key_press_handler(key=dpg.mvKey_Down, callback=log_key_press)
    dpg.add_key_press_handler(key=dpg.mvKey_Left, callback=log_key_press)
    dpg.add_key_press_handler(key=dpg.mvKey_Up, callback=log_key_press)

dpg.set_primary_window("primary_window", True)

dpg.setup_dearpygui()
# dpg.show_item_registry()
# dpg.show_style_editor()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

# ==== END MAIN ====

# table_data = [
#     {
#         "callout": "T-01",
#         "vendor": "Daltile",
#         "style": "Lorem Ipsum",
#         "color": "Beige",
#         "finish": "Polished",
#         "size": "12\"x48\"",
#         "thickness": "8mm",
#     },
#     {
#         "callout": "T-02",
#         "vendor": "Stone Source",
#         "style": "Lorem Ipsum",
#         "color": "Gray",
#         "finish": "Matte",
#         "size": "8\"x8\"",
#         "thickness": "10mm",
#     },
#     {
#         "callout": "T-03",
#         "vendor": "Emser",
#         "style": "Lorem Ipsum",
#         "color": "Absolute Black",
#         "finish": "Honed",
#         "size": "8\"X16\"",
#         "thickness": "9mm",
#     },
# ]