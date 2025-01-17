import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=400)

with dpg.window() as primary_window:
    with dpg.group(horizontal=True):
        with dpg.child_window(width=250, height=200):
            def _selection(sender, app_data, user_data):
                for item in user_data:
                    if item != sender:
                        dpg.set_value(item, False)
            items = (
                dpg.add_selectable(label="AECOM"),
                dpg.add_selectable(label="Build Group"),
                dpg.add_selectable(label="C.W. Driver"),
                dpg.add_selectable(label="Fairfield"),
                dpg.add_selectable(label="Hanover"),
                )

            for item in items:
                dpg.configure_item(item, callback=_selection, user_data=items)

        with dpg.child_window(border=False, height=200):
            # with dpg.menu_bar():
            #     dpg.add_menu_item(label="Manage")
            dpg.add_button(label="Add", width=55)
            dpg.add_button(label="Edit", width=55, enabled=False)
            dpg.add_button(label="Delete", width=55)
            dpg.add_button(label="Back", width=55)

    # dpg.add_separator()
    

    dpg.set_primary_window(primary_window, True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()