import dearpygui.dearpygui as dpg
from .ProjectListItem import ProjectListItem

class NewProjectModal:
    def __init__(self, projects_list:int|str):
        self.__projects_list = projects_list
        self.__width = 322
        self.__height = 127
        self.__pms = ["Clint", "Lisa", "Michael", "Jermey", "Rob", "Rymmy"]
        self.__gcs = ["AECOM", "Build Group", "C.W. Driver", "Fairfield", "Hanover"] # get from db in prod
        self.__select = ""

        with dpg.window(label="Create New Project", width=self.__width, autosize=True, min_size=[322, 80], modal=True, no_collapse=True, on_close=self.__reset_form, show=False) as self.__id:
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
                with dpg.child_window(width=240, height=200) as self.__gc_list:
                    for gc in self.__gcs:
                        dpg.add_selectable(label=gc, callback=self.__selection, user_data=gc)

                with dpg.child_window(border=False, height=200):
                    dpg.add_button(label="Add", callback=self.__render_gcm_input, user_data="add_btn", width=55)
                    dpg.add_button(label="Edit", callback=self.__render_gcm_input, enabled=False, user_data="edit_btn", width=55)
                    dpg.add_button(label="Delete", callback=self.__delete_gc, enabled=False, width=55)
                    dpg.add_button(label="Back", callback=self.__render_new_project_form, width=55)

            with dpg.group(show=False) as self.__gcm_input:
                with dpg.group(horizontal=True):
                    dpg.add_text("GC")
                    dpg.add_input_text(width=284)
                dpg.add_separator()
                with dpg.group(horizontal=True, indent=188):
                    dpg.add_button(label="Save", width=55)
                    dpg.add_button(label="Back", callback=self.__render_gcm, width=55)

    def __cancel(self):
        dpg.hide_item(self.__id)
        self.__reset_form()

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
        dpg.hide_item(self.__gcm_input)
        self.__set_title("GC Manager")
        dpg.show_item(self.__gcm)

    def __submit(self):
        if self.__is_filled_out():
            form_values = self.__get_values()
            # create a new project explorer list item and pass it the project explorer list id

            ProjectListItem(self.__projects_list, form_values["name"], form_values["gc"])

            self.__reset_form()
            self.__hide()
        else:
            self.__show_feedback()  

    def __reset_form(self):
        field_ids = self.__get_fields()
        for field, label in field_ids:
            dpg.set_value(field, "")
            dpg.configure_item(label, color=(255,255,255))
        dpg.hide_item(self._feedback_text_id)
        
        if not dpg.is_item_visible(self.__new_project_form):
            dpg.hide_item(self.__gcm)
            dpg.hide_item(self.__gcm_input)
            self.__set_title("Create New Project")
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

    def __render_gcm_input(self, sender, app_data, user_data):
        if user_data == "add_btn":
            self.__set_title("Add GC")
        elif user_data == "edit_btn":
            self.__set_title("Edit GC")

        dpg.hide_item(self.__gcm)
        dpg.show_item(self.__gcm_input)

    def __delete_gc(self):
        print("delete gc")

    def __render_new_project_form(self):
        x = int((dpg.get_viewport_width()/2) - (self.__width/2))
        y = int((dpg.get_viewport_height()/2) - (self.__height/2))

        dpg.hide_item(self.__gcm)
        self.__set_title("Create New Project")
        dpg.set_item_pos(self.__id, [x, y])
        dpg.show_item(self.__new_project_form)
        
    def __selection(self, sender, app_data, user_data):
        if not dpg.get_value(sender): # selectable value returns bool
            dpg.disable_item()
            dpg.disable_item() # <-- CONTINUE HERE
            
        items = dpg.get_item_children(self.__gc_list)[1]
        for item in items:
            if item != sender:
                dpg.set_value(item, False)

    def __set_title(self, title:str):
        dpg.set_item_label(self.__id, title)