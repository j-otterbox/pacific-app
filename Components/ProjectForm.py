import dearpygui.dearpygui as dpg
from .ProjectListItem import ProjectListItem
from Database import Database

class ProjectForm:
    def __init__(self):
        self.__width = 322
        self.__height = 127
        self._db = Database()
        self._pm_list = self._db.get_all_pms()
        self._gc_list = self._db.get_all_gcs()

        with dpg.stage() as self._stage_id:
            with dpg.group() as self.__new_project_form:
                with dpg.group(horizontal=True, horizontal_spacing=15):
                    with dpg.group(horizontal=True):
                        self._id_input_label = dpg.add_text("ID")
                        self._id_input_text = dpg.add_input_text(decimal=True, indent=36, width=55)
                    with dpg.group(horizontal=True):
                        self._pm_combo_label = dpg.add_text("PM")
                        pm_names = []
                        for pm in self._pm_list:
                            pm_names.append(pm["name"])
                        self._pm_combo = dpg.add_combo(pm_names, default_value="", width=80)

                with dpg.group(horizontal=True):
                    self._gc_combo_label = dpg.add_text("GC")
                    gc_names = []
                    for gc in self._gc_list:
                        gc_names.append(gc["name"])
                    self._gc_combo = dpg.add_combo(gc_names, default_value="", indent=36, width=184)
                    dpg.add_button(label="Manage GCs", callback=self.__render_gcm)

                with dpg.group(horizontal=True, horizontal_spacing=15):
                    with dpg.group(horizontal=True):
                        self._name_input_label = dpg.add_text("Name")
                        self._name_input_text = dpg.add_input_text(width=270)

                self._feedback_text = dpg.add_text("Please make sure all fields are entered.", color=(220,53,69), show=False)

                dpg.add_separator()

                with dpg.group(horizontal=True, indent=198):
                    self._create_project_btn = dpg.add_button(label="Create", callback=self._create_project_btn_handler)
                    self._cancel_btn = dpg.add_button(label="Cancel", callback=self._cancel_btn_handler)

    def _create_project_btn_handler(self):
        if self._is_form_completed():
            form_values = self._get_form_values()
            self._db.create_new_project(form_values)

            # create new project in database
            # should be on success only of previous task but
            # create a new project list item

        else:
            self._show_feedback()  

    def _is_form_completed(self): 
        for _, item in self._get_form_items():
            if dpg.get_value(item) == "": return False
        return True

    def _get_form_values(self):
        return {
            "id": dpg.get_value(self._id_input_text),
            "name": dpg.get_value(self._name_input_text),
            "gc": dpg.get_value(self._gc_combo),
            "pm": dpg.get_value(self._pm_combo)
        }

    def _get_form_items(self):
        return [
            (self._id_input_label, self._id_input_text),
            (self._pm_combo_label, self._pm_combo),
            (self._gc_combo_label, self._gc_combo),
            (self._name_input_label, self._name_input_text)
        ]

    def _show_feedback(self):
        form_items = self._get_form_items()
        for label, input in form_items:
            if dpg.get_value(input) == "":
                dpg.configure_item(label, color=(220,53,69))
            else:
                dpg.configure_item(label, color=(255,255,255))
        dpg.show_item(self._feedback_text)

    # def __reset_modal(self):
    #     form_items = self._get_form_inputs()
    #     for field, label in form_items:
    #         dpg.set_value(field, "")
    #         dpg.configure_item(label, color=(255,255,255))
    #     dpg.hide_item(self._feedback_text)

    def _cancel_btn_handler(self):
        dpg.hide_item(self._parent)
        dpg.delete_item(self._parent, children_only=True)

    def __render_gcm(self):
        x = int((dpg.get_viewport_width()/2) - (self.__width/2))
        y = int((dpg.get_viewport_height()/2) - (235/2))

        dpg.set_item_pos(self.__id, [x,y])
        dpg.hide_item(self.__new_project_form)
        dpg.hide_item(self.__gcm_form)
        self.__set_modal_title("GC Manager")
        dpg.show_item(self.__gcm)

        if not dpg.is_item_visible(self.__new_project_form):
            dpg.hide_item(self.__gcm)
            dpg.hide_item(self.__gcm_form)
            self.__set_modal_title("Create New Project")
            dpg.show_item(self.__new_project_form)

    def show(self):
        x = int((dpg.get_viewport_width()/2) - (self.__width/2))
        y = int((dpg.get_viewport_height()/2) - (self.__height/2))

        dpg.set_item_pos(self.__id, [x, y])
        dpg.show_item(self.__id)

    def render(self, parent):
        self._parent = parent
        dpg.push_container_stack(parent)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()