import dearpygui.dearpygui as dpg

class Table:
    def __init__(self):
        with dpg.staging_container() as self._staging_container_id:
            with dpg.group(horizontal=True):
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(tag="toggle_all_checkbox", callback=self._toggle_rows)
                    dpg.add_combo(tag="toggle_filter_combo", items=["None", "All"], callback=self._toggle_rows, default_value="None", fit_width=True)
                with dpg.group(tag="toggle_select_options", show=False, horizontal=True):
                    dpg.add_button(label="Delete Selected", callback=self._deleted_selected_rows)
                    dpg.add_button(label="Create Transmittal")
                    dpg.add_button(label="Gather Technical Docs")

            with dpg.group(horizontal=True):
                dpg.add_button(label="New Row", callback=self._add_new_row)
                dpg.add_button(label="Delete Row", callback=self._delete_row)
                dpg.add_text(tag="current_cell_text") # keep updated with the current cell

            with dpg.table(header_row=True, tag="spec_table", user_data=Table(9)):
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
                dpg.add_item_clicked_handler(callback=self._table_cell_clicked_handler)

    def _toggle_rows(self, item_id, item_value):
        caller_item_type = dpg.get_item_type(item_id)
        checkbox_ids = self._get_row_checkbox_ids()
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

    def _deleted_selected_rows(self):
        checkbox_ids = self._get_row_checkbox_ids()
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
                
        self._toggle_checkbox()
        dpg.set_value("toggle_all_checkbox", False)

    def _add_new_row(self, spec_data:dict):
        table_row_tags = dpg.get_item_children("spec_table")[1] # col 1  

        with dpg.table_row(parent="spec_table"):

            for j in range(0, 9):
                if j == 0:
                    row_idx_item_id = dpg.add_text(f"{len(table_row_tags)+1}", drop_callback=self._row_drop_handler, payload_type="str")

                    with dpg.drag_payload(parent=row_idx_item_id, drag_data="hello world", payload_type="str"):
                        dpg.add_text("dragging row # TBD")

                elif j == 1: # crow num
                    dpg.add_checkbox(callback=self._toggle_checkbox)
                else:
                    input_text_tag = dpg.add_input_text(width=-1)
                    dpg.bind_item_handler_registry(input_text_tag, "table_cell_handler")

    def _toggle_checkbox(self):
        checkbox_ids = self._get_row_checkbox_ids()

        for id in checkbox_ids:
            if dpg.get_value(id) == True:
                dpg.configure_item("toggle_select_options", show=True)
                return
        dpg.configure_item("toggle_select_options", show=False)

    def _row_drop_handler(self):
        print("yo ive been dropped")

    def _get_row_checkbox_ids(self):
        table_rows = dpg.get_item_children("spec_table")[1]
        checkbox_ids = []

        for row in table_rows:
            checkbox_ids.append(dpg.get_item_children(row)[1][1])

        return checkbox_ids

    def _delete_row():
        row_tags = dpg.get_item_children("spec_table")[1]

        if row_tags:
            dpg.delete_item(row_tags[-1])

    def _table_cell_clicked_handler(_, app_data):
        caller_cell_id = app_data[1]
        table_data = dpg.get_item_user_data("spec_table")
        table_row_ids = dpg.get_item_children("spec_table")[1]