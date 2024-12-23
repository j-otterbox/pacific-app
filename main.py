import dearpygui.dearpygui as dpg
from Models.SpecTable import SpecTable

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

# table data is assigned to the user-data slot of the table
# the arrow key handler will adjust the current cell

def table_cell_clicked_handler(_, app_data):
    caller_cell_id = app_data[1]
    table_data = dpg.get_item_user_data("spec_table")
    table_row_ids = dpg.get_item_children("spec_table")[1]

    # for row_idx, row_id in enumerate(table_row_ids):
    #     table_col_ids = list(dpg.get_item_children(row_id)[1])
    #     try:
    #         col_idx = table_col_ids.index(caller_cell_id)
    #         table_data.set_current_cell()
    #     except ValueError: # if id not found
    #         continue
        
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

    with dpg.table_row(parent="spec_table"):

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
    
def delete_row():
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
            dpg.add_button(label="Gather Technical Docs")

    with dpg.group(horizontal=True):
        dpg.add_button(label="New Row", callback=add_new_row)
        dpg.add_button(label="Delete Row", callback=delete_row)
        dpg.add_text(tag="current_cell_text") # keep updated with the current cell

    with dpg.table(header_row=True, tag="spec_table", user_data=SpecTable(9)):
        dpg.add_table_column(width_fixed=True)
        dpg.add_table_column(width_fixed=True)
        dpg.add_table_column(label="Callout")
        dpg.add_table_column(label="Vendor")
        dpg.add_table_column(label="Style")
        dpg.add_table_column(label="Color")
        dpg.add_table_column(label="Finish")
        dpg.add_table_column(label="Size")
        dpg.add_table_column(label="Thickness")

    with dpg.item_handler_registry(tag="table_cell_handler"):
        dpg.add_item_clicked_handler(callback=table_cell_clicked_handler)

def is_table_row(item_id):
    return dpg.get_item_type(item_id) == "mvAppItemType::mvTableRow"

def is_input_field(item_id):
    return dpg.get_item_type(item_id) == "mvAppItemType::mvInputText"

def key_press_handler():
    focused_item = dpg.get_focused_item() # x value
    focused_item_parent = dpg.get_item_parent(focused_item) # y value

    if is_input_field(focused_item) and is_table_row(focused_item_parent):
        table_data = dpg.get_item_user_data("spec_table")

        if dpg.is_key_pressed(dpg.mvKey_Right):
            table_data.shift_current_cell_right()
            
        elif dpg.is_key_pressed(dpg.mvKey_Down):
            table_data.shift_current_cell_down()

        elif dpg.is_key_pressed(key=dpg.mvKey_Left):
            table_data.shift_current_cell_left()

        elif dpg.is_key_pressed(key=dpg.mvKey_Up):
            table_data.shift_current_cell_up()

with dpg.handler_registry():
    dpg.add_key_press_handler(key=dpg.mvKey_Right, callback=key_press_handler)
    dpg.add_key_press_handler(key=dpg.mvKey_Down, callback=key_press_handler)
    dpg.add_key_press_handler(key=dpg.mvKey_Left, callback=key_press_handler)
    dpg.add_key_press_handler(key=dpg.mvKey_Up, callback=key_press_handler)

dpg.set_primary_window("primary_window", True)

dpg.setup_dearpygui()
# dpg.show_item_registry()
# dpg.show_style_editor()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

# ==== END MAIN ====