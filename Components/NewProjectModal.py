import dearpygui.dearpygui as dpg
from .ProjectListItem import ProjectListItem

class NewProjectModal:
    def __init__(self, projects_list:int|str):
        self.__projects_list = projects_list

        with dpg.window(label="New Project", show=False, autosize=True, on_close=self.__clear) as self.__id:
            with dpg.group() as self.__new_project_form:
                with dpg.group(horizontal=True, horizontal_spacing=15):
                    with dpg.group(horizontal=True):
                        self._id_field_label_id = dpg.add_text("ID")
                        self._id_field_id = dpg.add_input_text(decimal=True, width=60)
                    with dpg.group(horizontal=True):
                        self._name_field_label_id = dpg.add_text("Name")
                        self._name_field_id = dpg.add_input_text(width=227)
                with dpg.group(horizontal=True, horizontal_spacing=25):
                    with dpg.group(horizontal=True):
                        self._gc_field_label_id = dpg.add_text("GC")
                        self._gc_field_id = dpg.add_combo(["", "Fairfield", "Holland", "W.E. O'Neil"], width=130)
                        dpg.add_button(label="Manage GCs", callback=self.__render_gc_manager)
                    with dpg.group(horizontal=True):
                        self._pm_field_label_id = dpg.add_text("PM")
                        self._pm_field_id = dpg.add_combo(["", "Clint", "Lisa", "Michael", "Jermey", "Rob", "Rymmy"], width=75)

                self._feedback_text_id = dpg.add_text("Please make sure all fields have values entered.", color=(220,53,69), show=False)

                dpg.add_separator()

                with dpg.group(horizontal=True, indent=251):
                    self._submit_btn_id = dpg.add_button(label="Create", callback=self.__submit)
                    self._cancel_btn_id = dpg.add_button(label="Cancel", callback=self.__cancel)

            with dpg.group(horizontal=True, show=False) as self.__gc_manager:
                with dpg.child_window(width=250, height=100):

                    items = (
                        dpg.add_selectable(label="AECOM"),
                        dpg.add_selectable(label="Build Group"),
                        dpg.add_selectable(label="C.W. Driver"),
                        dpg.add_selectable(label="Fairfield"),
                        dpg.add_selectable(label="Hanover"),
                        )

                    for item in items:
                        dpg.configure_item(item, callback=self.__selection, user_data=items)

                with dpg.child_window(border=False, height=200):
                    dpg.add_button(label="Add", width=55, callback=self.__add_btn_handler)
                    with dpg.window(label="Add New GC", show=False) as self.__add_gc_window:
                        with dpg.group(horizontal=True):
                            dpg.add_text("Name")
                            dpg.add_input_text()
                            dpg.add_button(label="Save")

                    dpg.add_button(label="Edit", width=55, callback=self.__edit_btn_handler)
                    dpg.add_button(label="Delete", width=55, callback=self.__delete_btn_handler)
                    dpg.add_button(label="Back", width=55, callback=self.__back_btn_handler)

    def __cancel(self):
        dpg.hide_item(self.__id)
        self.__clear()

    def __get_field_ids(self):
        return [
            (self._id_field_id, self._id_field_label_id),
            (self._name_field_id, self._name_field_label_id),
            (self._gc_field_id, self._gc_field_label_id),
            (self._pm_field_id, self._pm_field_label_id)
        ]

    def __render_gc_manager(self):
        dpg.hide_item(self.__new_project_form)
        self.__set_title("GC Manager")
        dpg.show_item(self.__gc_manager)
        
    def __submit(self):
        if self.__is_filled_out():
            form_values = self.__get_values()
            # create a new project explorer list item and pass it the project explorer list id

            ProjectListItem(self.__projects_list, form_values["name"], form_values["gc"])

            self.__clear()
            self.__hide()
        else:
            self.__show_feedback()  

    def __clear(self):
        field_ids = self.__get_field_ids()
        for field, _ in field_ids:
            dpg.set_value(field, "")
        dpg.hide_item(self._feedback_text_id)
        
        if not dpg.is_item_visible(self.__new_project_form):
            dpg.show_item(self.__new_project_form)
            dpg.hide_item(self.__gc_manager)


    def __is_filled_out(self):
        field_ids = self.__get_field_ids()
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
        field_ids = self.__get_field_ids()

        for field, label in field_ids:
            if dpg.get_value(field) == "":
                dpg.configure_item(label, color=(220,53,69))
            else:
                dpg.configure_item(label, color=(255,255,255))

        dpg.show_item(self._feedback_text_id)

    def __hide(self):
        dpg.hide_item(self.__id)

    def show(self):
        dpg.show_item(item=self.__id)

    def __add_btn_handler(self):
        dpg.show_item(self.__add_gc_window)

    def __edit_btn_handler(self):
        print("edit gc")

    def __delete_btn_handler(self):
        print("delete gc")

    def __back_btn_handler(self):
        dpg.hide_item(self.__gc_manager)
        self.__set_title("New Project")
        dpg.show_item(self.__new_project_form)

    def __selection(self, sender, app_data, user_data):
        for item in user_data:
            if item != sender:
                dpg.set_value(item, False)

    def __set_title(self, title:str):
        dpg.set_item_label(self.__id, title)