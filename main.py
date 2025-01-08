import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Pacific Carpets', width=1200, height=800)

with dpg.window(tag="primary_window"):
    pass

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