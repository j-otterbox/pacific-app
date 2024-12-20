import dearpygui.dearpygui as dpg

# - basic database for samples 
# - TODO: needs CRUD functionality
# - CREATE (ui only)
# - READ
# - UPDATE
# - DELETE (ui only)
# - TODO: options that can be applied to toggle selections (delete)

# - basic information about the samples is tracked (callout, vendor, style, etc.)
# - need to track: status, ETA if samples ordered, data gathered
# - later: transmittals should be able to be created from here
# - should be able to filter table, group by vendor,

table_data = {
    "current_cell": [0,0],
    "rows": [
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
}

def get_row_checkbox_ids():
    table_rows = dpg.get_item_children("spec_table")[1]
    checkbox_ids = []

    for row in table_rows:
        checkbox_ids.append(dpg.get_item_children(row)[1][1])

    return checkbox_ids

def toggle_checkbox():
    checkbox_ids = get_row_checkbox_ids()

    for id in checkbox_ids:
        if dpg.get_value(id) == True:
            dpg.configure_item("toggle_select_options", show=True)
            return
    dpg.configure_item("toggle_select_options", show=False)

def row_drag_handler():
    print("yo im being dragged")

def row_drop_handler():
    print("yo ive been dropped")

def add_new_row(spec_data:dict):
    table_row_tags = dpg.get_item_children("spec_table")[1] # col 1  

    with dpg.table_row(parent="spec_table") as table_row_tag:

        for j in range(0, 9):
            if j == 0:
                row_idx_item_id = dpg.add_text(f"{len(table_row_tags)+1}", drop_callback=row_drop_handler, payload_type="str")

                with dpg.drag_payload(parent=row_idx_item_id, drag_data="hello world", payload_type="str"):
                    dpg.add_text("dragging row # TBD")

            elif j == 1: # crow num
                dpg.add_checkbox(callback=toggle_checkbox)
            else:
                input_text_tag = dpg.add_input_text(width=-1)



                dpg.bind_item_handler_registry(input_text_tag, "table_cell_handler")

    # if not current_cell:
    #     current_cell = [0,0]

def deleted_selected_rows():
    checkbox_ids = get_row_checkbox_ids()
    row_idx = 0

    # if the row is NOT deleted, adjust its row number in the table
    for checkbox_id in checkbox_ids:
        parent_id = dpg.get_item_parent(checkbox_id)

        if dpg.get_value(checkbox_id) == True: 
            dpg.delete_item(parent_id)
        else:
            row_idx += 1
            row_idx_cell = dpg.get_item_children(parent_id)[1][0]
            dpg.set_value(row_idx_cell, row_idx)
            
    toggle_checkbox()
    dpg.set_value("toggle_all_checkbox", False)
    
def delete_row(table_row_tag:int):
    row_tags = dpg.get_item_children("spec_table")[1]

    if row_tags:
        dpg.delete_item(row_tags[-1])

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

            dpg.configure_item("toggle_select_options", show=False)

    elif toggle_filter == "All":

        if caller_item_type == "mvAppItemType::mvCheckbox":
            dpg.set_value("toggle_all_checkbox", toggle_checkbox_value)
            for id in checkbox_ids:
                dpg.set_value(id, toggle_checkbox_value)

            dpg.configure_item("toggle_select_options", show=toggle_checkbox_value)

        elif caller_item_type == "mvAppItemType::mvCombo":
            dpg.set_value("toggle_all_checkbox", True)
            for id in checkbox_ids:
                dpg.set_value(id, True)

            dpg.configure_item("toggle_select_options", show=True)

# ==== BEGIN MAIN ====

dpg.create_context()
dpg.create_viewport(title='Pacific Carpets', width=1200, height=800)

with dpg.window(tag="primary_window"):
    with dpg.group(horizontal=True):
        with dpg.group(horizontal=True):
            dpg.add_checkbox(tag="toggle_all_checkbox", callback=toggle_rows)
            dpg.add_combo(tag="toggle_filter_combo", items=["None", "All"], callback=toggle_rows, default_value="None", fit_width=True)
        with dpg.group(tag="toggle_select_options", show=False, horizontal=True):
            dpg.add_button(label="Delete Selected", callback=deleted_selected_rows)
            dpg.add_button(label="Create Transmittal")

    with dpg.group(horizontal=True):
        dpg.add_button(label="New Row", callback=add_new_row)
        dpg.add_button(label="Delete Row", callback=delete_row)

    with dpg.table(header_row=True, tag="spec_table", user_data=table_data) as table_tag:

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

        # with dpg.item_handler_registry(tag="table_cell_handler"):
        #     dpg.add_item_deactivated_handler(callback=deactivated_handler)


def log_key_press(e, c):
    """ 
        table user-data shoulda handle the operation of tracking the current cell internally,
        will have to get parents(rows), and children (cols) to update the active cell after
        updating the current cell 
    """


    if dpg.is_key_pressed(dpg.mvKey_Right):
        print("right arrow pressed")

        x, y = dpg.get_item_user_data("spec_table")["current_cell"]
    
        # x value cannot exceed number of columns

    elif dpg.is_key_pressed(dpg.mvKey_Down):
        print("down arrow pressed")

        # y value cannot exceed number of rows

    elif dpg.is_key_pressed(key=dpg.mvKey_Left):
        print("left arrow pressed")

        # x value cannot be less than 0

    elif dpg.is_key_pressed(key=dpg.mvKey_Up):
        print("up arrow pressed")

        # y value cannot be less than 0

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