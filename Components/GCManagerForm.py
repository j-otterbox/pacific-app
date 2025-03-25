import dearpygui.dearpygui as dpg

class GCManagerForm:
    def __init__(self):
        with dpg.stage() as stage_id:
            with dpg.group(horizontal=True, show=False) as self.__gcm:
                with dpg.child_window(width=240, height=200) as self.__gcm_list:
                    for gc in self.__gcs:
                        dpg.add_selectable(label=gc, callback=self.__on_gcm_list_selection, user_data=gc)

                with dpg.child_window(border=False, height=200):
                    self.__gcm_add_btn = dpg.add_button(label="Add", callback=self.__render_gcm_form, width=55)
                    self.__gcm_edit_btn = dpg.add_button(label="Edit", callback=self.__render_gcm_form, enabled=False, width=55)
                    self.__gcm_delete_btn = dpg.add_button(label="Delete", callback=self.__on_gcm_delete_btn_click, enabled=False, width=55)
                    dpg.add_button(label="Back", callback=self.__render_new_project_form, width=55)

    def __render_gcm_form(self, sender):
        if sender == self.__gcm_add_btn:
            self.__set_modal_title("Add GC")
            dpg.set_value(self.__gcm_text_input, "")
            dpg.set_item_user_data(self.__gcm_form_submit_btn, "add")

        elif sender == self.__gcm_edit_btn:
            self.__set_modal_title("Edit GC")
            items = dpg.get_item_children(self.__gcm_list)[1]
            for item in items: 
                if dpg.get_value(item):
                    dpg.set_value(self.__gcm_text_input, dpg.get_item_user_data(item))
                    break
            dpg.set_item_user_data(self.__gcm_form_submit_btn, "edit")
                
        dpg.hide_item(self.__gcm)
        dpg.show_item(self.__gcm_form)

    def __on_gcm_delete_btn_click(self):
        pass
        # get the selected item value
        # self.__gcs.remove()
        # update the list ui

    def __render_new_project_form(self):
        x = int((dpg.get_viewport_width()/2) - (self.__width/2))
        y = int((dpg.get_viewport_height()/2) - (self.__height/2))

        items = dpg.get_item_children(self.__gcm_list)[1]
        for item in items:
            dpg.set_value(item, False)

        dpg.hide_item(self.__gcm)
        self.__set_modal_title("Create New Project")
        dpg.set_item_pos(self.__id, [x, y])
        dpg.hide_item(self.__gcm_form_feedback)
        dpg.show_item(self.__new_project_form)

    def __on_gcm_list_selection(self, sender): 
        list_item_selected = dpg.get_value(sender)

        if list_item_selected:
            dpg.enable_item(self.__gcm_edit_btn)
            dpg.enable_item(self.__gcm_delete_btn)
        else:
            dpg.disable_item(self.__gcm_edit_btn)
            dpg.disable_item(self.__gcm_delete_btn)

        items = dpg.get_item_children(self.__gcm_list)[1] # deselect the rest
        for item in items:
            if item != sender:
                dpg.set_value(item, False)

    def render(self):
        pass