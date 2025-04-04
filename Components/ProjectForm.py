import dearpygui.dearpygui as dpg
from Database import Database
from Components.ManagerForm import ManagerForm

class ProjectForm:
    def __init__(self):
        self._db = Database()
        self._mgr_form = ManagerForm()
        self._mgr_form.set_back_btn_callback(self._return_to_proj_form)
        
        with dpg.stage() as self._stage_id:
            with dpg.group(horizontal=True):
                self._job_id_input_label = dpg.add_text("Job ID")
                self._job_id_text_input = dpg.add_input_text(decimal=True, width=55)
            with dpg.group(horizontal=True):
                self._pm_combo_label = dpg.add_text("PM", indent=28)
                pm_names = []
                for pm in self._db.get_all_project_mgrs():
                    pm_names.append(pm["name"])
                self._pm_combo = dpg.add_combo(pm_names, default_value="", width=184)
                dpg.add_button(label="Manage PMs", callback=self._manage_pms_btn_click_handler)
            with dpg.group(horizontal=True):
                self._gc_combo_label = dpg.add_text("GC", indent=28)
                gc_names = []
                for gc in self._db.get_all_gen_contractors():
                    gc_names.append(gc["name"])
                self._gc_combo = dpg.add_combo(gc_names, default_value="", width=184)
                dpg.add_button(label="Manage GCs", callback=self._manage_gcs_btn_click_handler)
            with dpg.group(horizontal=True):
                self._name_input_label = dpg.add_text("Name", indent=14)
                self._name_text_input = dpg.add_input_text(width=-1)
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

    def _get_form_values(self):
        return {
            "job_id": dpg.get_value(self._job_id_text_input),
            "pm": dpg.get_value(self._pm_combo),
            "gc": dpg.get_value(self._gc_combo),
            "name": dpg.get_value(self._name_text_input)
        }

    def _is_form_completed(self) -> bool: 
        for _, input in self._get_form_items():
            if dpg.get_value(input) == "": return False
        return True

    def _get_form_items(self):
        return [
            (self._job_id_input_label, self._job_id_text_input),
            (self._pm_combo_label, self._pm_combo),
            (self._gc_combo_label, self._gc_combo),
            (self._name_input_label, self._name_text_input)
        ]

    def _show_feedback(self):
        form_items = self._get_form_items()
        for label, input in form_items:
            if dpg.get_value(input) == "":
                dpg.configure_item(label, color=(220,53,69))
            else:
                dpg.configure_item(label, color=(255,255,255))
        dpg.show_item(self._feedback_text)

    def _manage_gcs_btn_click_handler(self):
        dpg.delete_item(self._parent, children_only=True)
        self._mgr_form.clear()
        self._mgr_form.render(self._parent)
        
    def _manage_pms_btn_click_handler(self):
        pass

    def _cancel_btn_handler(self):
        dpg.hide_item(self._parent)        
        dpg.delete_item(self._parent, children_only=True)

    def _return_to_proj_form(self) -> None:
        """ Callback for back button of the GC Manager. """
        dpg.set_item_label(self._parent, "Create New Project")
        dpg.delete_item(self._parent, children_only=True)
        dpg.configure_item(self._pm_combo, default_value="")
        dpg.configure_item(self._gc_combo, default_value="")
        self._update_pm_combo()
        self._update_gc_combo()
        self.render(self._parent)

    def _update_pm_combo(self):
        pm_names = []
        for pm in self._db.get_all_project_mgrs():
            pm_names.append(pm["name"])
        dpg.configure_item(self._pm_combo, items=pm_names)

    def _update_gc_combo(self) -> None:
        """ Updates GC dropdown with the most recent. """
        gc_names = []
        for gc in self._db.get_all_gen_contractors():
            gc_names.append(gc["name"])
        dpg.configure_item(self._gc_combo, items=gc_names)

    # PUBLIC

    def clear(self) -> None:
        """ Sets the form back to its default state. """
        form_items = self._get_form_items()
        for label, input in form_items:
            dpg.configure_item(label, color=(255,255,255))
            dpg.set_value(input, "")
        dpg.hide_item(self._feedback_text)

    def render(self, parent:int|str) -> None:
        """ Unstages the component as a child of the parent item. """
        self._parent = parent
        dpg.push_container_stack(self._parent)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()

    def set_projects_list_id(self, id:int|str) -> None:
        """ Sets the parent for newly created project items, should be the project explorer. """
        self._projects_list = id

    # def __render_gcm(self):
    #     x = int((dpg.get_viewport_width()/2) - (self.__width/2))
    #     y = int((dpg.get_viewport_height()/2) - (235/2))

    #     dpg.set_item_pos(self.__id, [x,y])
 
    # def show(self):
    #     x = int((dpg.get_viewport_width()/2) - (self.__width/2))
    #     y = int((dpg.get_viewport_height()/2) - (self.__height/2))

    #     dpg.set_item_pos(self.__id, [x, y])
    #     dpg.show_item(self.__id)
