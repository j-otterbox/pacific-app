import dearpygui.dearpygui as dpg
from .ProjectListItem import ProjectListItem

class NewProjectModal:
    def __init__(self, projects_list:int|str):
        self.__projects_list = projects_list
        self.__width = 322
        self.__height = 127
        self.__pms = ["Clint", "Lisa", "Michael", "Jermey", "Rob", "Rymmy"]
        self.__gcs = ["AECOM", "Build Group", "C.W. Driver", "Fairfield", "Hanover"] # get from db in prod

        with dpg.window(label="Create New Project", width=self.__width, autosize=True, min_size=[322, 80], modal=True, no_collapse=True, on_close=self.__reset_modal, show=False) as self.__id:
            with dpg.group() as self.__new_project_form:
                with dpg.group(horizontal=True, horizontal_spacing=15):
                    with dpg.group(horizontal=True):
                        self._id_field_label_id = dpg.add_text("ID")
                        self._id_field_id = dpg.add_input_text(decimal=True, indent=36, width=55)
                    with dpg.group(horizontal=True):
                        self._pm_field_label_id = dpg.add_text("PM")
                        self._pm_field_id = dpg.add_combo(self.__pms, default_value="", width=80)

                with dpg.group(horizontal=True):
                    self._gc_field_label_id = dpg.add_text("GC")
                    self._gc_field_id = dpg.add_combo(self.__gcs, default_value="", indent=36, width=184)
                    dpg.add_button(label="Manage GCs", callback=self.__render_gcm)

                with dpg.group(horizontal=True, horizontal_spacing=15):
                    with dpg.group(horizontal=True):
                        self._name_field_label_id = dpg.add_text("Name")
                        self._name_field_id = dpg.add_input_text(width=270)

                self._feedback_text_id = dpg.add_text("Please make sure all fields are entered.", color=(220,53,69), show=False)

                dpg.add_separator()

                with dpg.group(horizontal=True, indent=198):
                    self._submit_btn_id = dpg.add_button(label="Create", callback=self.__submit)
                    self._cancel_btn_id = dpg.add_button(label="Cancel", callback=self.__cancel)

            with dpg.group(horizontal=True, show=False) as self.__gcm:
                with dpg.child_window(width=240, height=200) as self.__gcm_list:
                    for gc in self.__gcs:
                        dpg.add_selectable(label=gc, callback=self.__on_gcm_list_selection, user_data=gc)

                with dpg.child_window(border=False, height=200):
                    self.__gcm_add_btn = dpg.add_button(label="Add", callback=self.__render_gcm_form, width=55)
                    self.__gcm_edit_btn = dpg.add_button(label="Edit", callback=self.__render_gcm_form, enabled=False, width=55)
                    self.__gcm_delete_btn = dpg.add_button(label="Delete", callback=self.__on_gcm_delete_btn_click, enabled=False, width=55)
                    dpg.add_button(label="Back", callback=self.__render_new_project_form, width=55)

            with dpg.group(show=False) as self.__gcm_form:
                with dpg.group(horizontal=True):
                    dpg.add_text("Name")
                    self.__gcm_text_input = dpg.add_input_text(width=270)
                self.__gcm_form_feedback = dpg.add_text(color=(220,53,69), show=False)
                dpg.add_separator()
                with dpg.group(horizontal=True, indent=188):
                    self.__gcm_form_submit_btn = dpg.add_button(label="Save", callback=self.__on_gcm_form_submit, width=55)
                    dpg.add_button(label="Back", callback=self.__render_gcm, width=55)

    def __cancel(self):
        dpg.hide_item(self.__id)
        self.__reset_modal()

    def __get_fields(self):
        return [
            (self._id_field_id, self._id_field_label_id),
            (self._name_field_id, self._name_field_label_id),
            (self._gc_field_id, self._gc_field_label_id),
            (self._pm_field_id, self._pm_field_label_id)
        ]

    def __render_gcm(self):
        x = int((dpg.get_viewport_width()/2) - (self.__width/2))
        y = int((dpg.get_viewport_height()/2) - (235/2))

        dpg.set_item_pos(self.__id, [x,y])
        dpg.hide_item(self.__new_project_form)
        dpg.hide_item(self.__gcm_form)
        self.__set_modal_title("GC Manager")
        dpg.show_item(self.__gcm)

    def __submit(self):
        if self.__is_filled_out():
            form_values = self.__get_values()
            # create a new project explorer list item and pass it the project explorer list id

            ProjectListItem(self.__projects_list, form_values["name"], form_values["gc"])

            self.__reset_modal()
            self.__hide()
        else:
            self.__show_feedback()  

    def __reset_modal(self):
        field_ids = self.__get_fields()
        for field, label in field_ids:
            dpg.set_value(field, "")
            dpg.configure_item(label, color=(255,255,255))
        dpg.hide_item(self._feedback_text_id)
        
        if not dpg.is_item_visible(self.__new_project_form):
            dpg.hide_item(self.__gcm)
            dpg.hide_item(self.__gcm_form)
            self.__set_modal_title("Create New Project")
            dpg.show_item(self.__new_project_form)

    def __is_filled_out(self): 
        field_ids = self.__get_fields()
        for field, _ in field_ids:
            if dpg.get_value(field) == "": return False
        return True

    def __get_values(self):
        return {
            "id": dpg.get_value(self._id_field_id),
            "name": dpg.get_value(self._name_field_id),
            "gc": dpg.get_value(self._gc_field_id),
            "pm": dpg.get_value(self._pm_field_id)
        }

    def __show_feedback(self):
        field_ids = self.__get_fields()

        for field, label in field_ids:
            if dpg.get_value(field) == "":
                dpg.configure_item(label, color=(220,53,69))
            else:
                dpg.configure_item(label, color=(255,255,255))

        dpg.show_item(self._feedback_text_id)

    def __hide(self):
        dpg.hide_item(self.__id)

    def show(self):
        x = int((dpg.get_viewport_width()/2) - (self.__width/2))
        y = int((dpg.get_viewport_height()/2) - (self.__height/2))

        dpg.set_item_pos(self.__id, [x, y])
        dpg.show_item(self.__id)

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

    def __on_gcm_form_submit(self, sender, app_data, user_data):
        input_value = dpg.get_value(self.__gcm_text_input)
        form_action = user_data

        if not input_value:
            dpg.set_value(self.__gcm_form_feedback, "Form input has no value entered.")
            dpg.show_item(self.__gcm_form_feedback)
            return
            
        if form_action == "add":
            if self.__gcs.count(input_value) > 0:
                dpg.set_value(self.__gcm_form_feedback, "GC already exists.")
                dpg.show_item(self.__gcm_form_feedback)
                return
            
            insert_idx = -1
            for idx, gc in enumerate(self.__gcs):
                if str.lower(input_value) < str.lower(gc):
                    insert_idx = idx
                    break

            if insert_idx >= 0:
                self.__gcs.insert(insert_idx, input_value)
            else: self.__gcs.append(input_value)

            print(self.__gcs)

            items = dpg.get_item_children(self.__gcm_list)[1]
            
            if insert_idx >= 0:
                dpg.add_selectable(label=input_value, before=items[insert_idx],  callback=self.__on_gcm_list_selection, user_data=input_value)
            else: 
                dpg.add_selectable(parent=self.__gcm_list, label=input_value, callback=self.__on_gcm_list_selection, user_data=input_value)
            self.__render_gcm()
            
            # get id of the list item at the insert_idx
            # add one to it, get that items id.
            # set the before property of the new selectable to that id
            # if adding one puts it out of range, set the parent to the gc_list as the before property is not needed


        if form_action == "edit":
            pass

            # confirm the form has a value
            # get the id of the currently selected list item
            # update that list item with the current value whatever it is
            # specifically update

    def __set_modal_title(self, title:str):
        dpg.set_item_label(self.__id, title)