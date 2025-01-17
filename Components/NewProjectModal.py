import dearpygui.dearpygui as dpg
from .ProjectListItem import ProjectListItem

# TODO: when form is submitted, item is added to list
# TODO: get gc manager to work

class NewProjectModal:
    def __init__(self, projects_list:int|str):
        self.__projects_list = projects_list

        with dpg.window(label="New Project", modal=True, show=False, autosize=True, on_close=self.__clear) as self.__id:
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

    # private methods

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
        print("i open the gc manager")

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

    # public methods

    def show(self):
        dpg.show_item(item=self.__id)