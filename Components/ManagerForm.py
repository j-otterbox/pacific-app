import dearpygui.dearpygui as dpg
from Database import Database
from collections.abc import Callable
from Components.InputTextForm import InputTextForm
from Components.ConfirmationForm import ConfirmationForm

class ManagerForm:
    def __init__(self):
        """ 
            User interface for managing project managers and general contractors. 
        """
        self._db = Database()
        self._data = []
        self._input_form = InputTextForm(input_label="Name", cancel_btn_callback=self._return_to_gc_manager)
        self._confirmation_form = ConfirmationForm(cancel_btn_callback=self._return_to_gc_manager)

        with dpg.stage() as self._stage_id:
            with dpg.group(horizontal=True):
                with dpg.child_window(width=240, height=200) as self._selectables_list:
                    pass
                    # for gc in self._gc_data:
                    #     dpg.add_selectable(label=gc["name"], user_data=gc, callback=self._selectable_click_handler)

                with dpg.child_window(border=False, height=200):
                    self._add_btn = dpg.add_button(label="Add", callback=self._add_btn_click_handler, width=55)
                    self._edit_btn = dpg.add_button(label="Edit", callback=self._edit_btn_click_handler, enabled=False, width=55)
                    self._delete_btn = dpg.add_button(label="Delete", callback=self._delete_btn_click_handler, enabled=False, width=55)
                    self._back_btn = dpg.add_button(label="Back", width=55)

    def set_form_mode(self, mode:str) -> None:
        """ Toggles the function of the form between two states, PM and GC. """
        dpg.delete_item(self._selectables_list, children_only=True)
        if mode == "pm":
            self._init_pm_manager()
        elif mode == "gc":
            self._init_gc_manager()
        else: raise Exception(f"Unexpected arg supplied to parameter 'mode'. Expected 'pm' or 'gc', instead received {mode}.")
        
    def _init_pm_manager(self):
        dpg.set_item_label(self._parent, "PM Manager")
        self._data = self._db.get_all_project_mgrs()
        for pm in self._data:
            dpg.add_selectable(
                parent=self._selectables_list,
                label=pm["name"],
                callback=self._selectable_click_handler,
                user_data=pm
            )
            dpg.set_item_callback(self._add_btn)
            dpg.set_item_callback(self._edit_btn)
            dpg.set_item_callback(self._delete_btn)

    def _init_gc_manager(self):
        dpg.set_item_label(self._parent, "GC Manager")
        self._data = self._db.get_all_gen_contractors() # get data
        for gc in self._data: # populate list
            dpg.add_selectable(
                parent=self._selectables_list,
                label=gc["name"],
                callback=self._selectable_click_handler,
                user_data=gc
            )
            dpg.set_item_callback(self._add_btn)
            dpg.set_item_callback(self._edit_btn)
            dpg.set_item_callback(self._delete_btn)

    def _selectable_click_handler(self, sender) -> None:
        """ Toggles selectable on/off, only one item toggled on max. """
        self._toggled_selectable = dpg.get_value(sender)
        
        if self._toggled_selectable:
            dpg.enable_item(self._edit_btn)
            dpg.enable_item(self._delete_btn)
        else:
            dpg.disable_item(self._edit_btn)
            dpg.disable_item(self._delete_btn)

        selectables = dpg.get_item_children(self._selectables_list)[1]
        for item in selectables:
            if item != sender:
                dpg.set_value(item, False)

    def _add_btn_click_handler(self) -> None:
        """ Preps and renders the form for creating new general contractors. """
        dpg.set_item_label(self._parent, "Create New GC")
        dpg.delete_item(self._parent, children_only=True)
        self._input_form.clear()
        self._input_form.set_save_btn_callback(self._save_new_gc)
        self._input_form.render(self._parent)

    def _save_new_gc(self) -> None:
        """
            Creates a new GC and returns a response from the database.
        """
        user_input = self._input_form.get_value()

        if not user_input:
            self._input_form.set_feedback("Form is not filled out.")
            self._input_form.show_feedback()
        else:
            resp = self._db.create_gen_contractor(user_input)

            if resp["success"]:
                new_gc = resp["data"][0]
                self._gc_data.append(new_gc)
                self._update_gc_selectables()
                self._return_to_gc_manager()
            else:
                self._input_form.set_feedback(resp["msg"])
                self._input_form.show_feedback()

    def _edit_btn_click_handler(self) -> None:
        """ 
            Preps and renders the form with the selected general contractor for updating.
        """
        dpg.set_item_label(self._parent, "Edit GC")
        dpg.delete_item(self._parent, children_only=True)
        gc_name = dpg.get_item_user_data(self._toggled_selectable)["name"]
        self._input_form.set_value(gc_name)
        self._input_form.set_save_btn_callback(self._save_gc_edit_handler)        
        self._input_form.render(self._parent)

    def _save_gc_edit_handler(self) -> None:
        """ Commits the current form value updating the selected general contractor. """
        selected_gc = dpg.get_item_user_data(self._toggled_selectable)
        user_input = self._input_form.get_value()

        if user_input != selected_gc["name"]:
            self._db.update_gc(selected_gc["id"], user_input)
            selected_gc["name"] = user_input
            dpg.set_item_user_data(self._toggled_selectable, selected_gc)
            dpg.set_item_label(self._toggled_selectable, user_input)
            self._return_to_gc_manager()

    def _delete_btn_click_handler(self):
        dpg.set_item_label(self._parent, "Confirm Delete")
        dpg.delete_item(self._parent, children_only=True)
        gc_name = dpg.get_item_user_data(self._toggled_selectable)["name"]
        self._confirmation_form.set_prompt(f"Are you sure you want to delete GC '{gc_name}'?")
        self._confirmation_form.set_confirm_callback(self._delete_gc)
        self._confirmation_form.render(self._parent)

    def _delete_gc(self):
        selected_gc = dpg.get_item_user_data(self._toggled_selectable)
        self._db.delete_gen_contractor(selected_gc["id"])
        for idx, gc in enumerate(self._gc_data):
            if selected_gc["id"] == gc["id"]:
                self._gc_data.pop(idx)
                break
        self._update_gc_selectables()
        self._return_to_gc_manager()

    def _update_gc_selectables(self):
        self._data.sort(key=lambda elem : elem["name"])
        dpg.delete_item(self._selectables_list, children_only=True)
        for elem in self._data:
            dpg.add_selectable(
                label=elem["name"],
                parent=self._selectables_list,
                callback=self._selectable_click_handler,
                user_data=elem
            )

    def _return_to_gc_manager(self) -> None:
        """ 
            To be passed to the add/edit/delete forms as a handler
            when the user completes or cancels any operation.
        """
        dpg.set_item_label(self._parent, "GC Manager")
        dpg.delete_item(self._parent, children_only=True)
        self.render(self._parent)

    def set_back_btn_callback(self, callback:Callable) -> None:
        """ Sets the back btn callback which should be provided by the parent component. """
        dpg.set_item_callback(self._back_btn, )
        
    def clear(self):
        """ Sets the GC Manager form to it's default state, no items selected. """
        selectables = dpg.get_item_children(self._selectables_list)[1]
        for item in selectables:
            dpg.set_value(item, False)
        self._toggled_selectable = None
        dpg.disable_item(self._edit_btn)
        dpg.disable_item(self._delete_btn)

    def render(self, parent):
        self._parent = parent
        dpg.push_container_stack(self._parent)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()

    # ProjectForm.render(self._parent)
    # x = int((dpg.get_viewport_width()/2) - (self.__width/2))
    # y = int((dpg.get_viewport_height()/2) - (self.__height/2))
    # dpg.set_item_pos(self.__id, [x, y])
