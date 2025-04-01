import dearpygui.dearpygui as dpg
from Database import Database
from collections.abc import Callable
from Components.InputTextForm import InputTextForm
from Components.ConfirmationForm import ConfirmationForm

class GCManagerForm:
    def __init__(self, back_btn_callback: Callable=None):
        self._db = Database()
        self._gc_list = self._db.get_all_gen_contractors()
        self._input_form = InputTextForm(input_label="Name", cancel_btn_callback=self._return_to_gc_manager)
        self._confirmation_form = ConfirmationForm(cancel_btn_callback=self._return_to_gc_manager)

        with dpg.stage() as self._stage_id:
            with dpg.group(horizontal=True):
                with dpg.child_window(width=240, height=200) as self._selectables_container:
                    for gc in self._gc_list:
                        dpg.add_selectable(label=gc["name"], user_data=gc, callback=self._gc_selectable_handler)

                with dpg.child_window(border=False, height=200):
                    self._add_gc_btn = dpg.add_button(label="Add", callback=self._add_btn_handler, width=55)
                    self._update_gc_btn = dpg.add_button(label="Edit", callback=self._edit_btn_handler, enabled=False, width=55)
                    self._delete_gc_btn = dpg.add_button(label="Delete", callback=self._delete_btn_handler, enabled=False, width=55)
                    if back_btn_callback is not None:
                        self._back_btn = dpg.add_button(label="Back", callback=back_btn_callback, width=55)

    def _add_btn_handler(self) -> None:
        """ Preps and renders the form for creating new general contractors. """
        dpg.set_item_label(self._parent, "Create New GC")
        dpg.delete_item(self._parent, children_only=True)
        self._input_form.clear()
        self._input_form.set_save_btn_callback(self._create_gc)
        self._input_form.render(self._parent)

    def _create_gc(self) -> None:
        """
            Commits the current form value with the new general 
            contractor and handles the success/failure of the query.
        """
        user_input = self._input_form.get_value()

        if not user_input:
            self._input_form.set_feedback("Form is not filled out.")
            self._input_form.show_feedback()
        else:
            resp = self._db.create_gen_contractor(user_input)

            if resp["success"]:
                new_gc = resp["data"][0]
                self._gc_list.append(new_gc)
                self._update_gc_selectables()
                self._return_to_gc_manager()
            else:
                self._input_form.set_feedback(resp["msg"])
                self._input_form.show_feedback()

    def _edit_btn_handler(self) -> None:
        """ 
            Preps and renders the form with the selected general contractor for updating.
        """
        dpg.set_item_label(self._parent, "Edit GC")
        dpg.delete_item(self._parent, children_only=True)
        gc_name = dpg.get_item_user_data(self._selected_list_item)["name"]
        self._input_form.set_value(gc_name)
        self._input_form.set_save_btn_callback(self._update_gc)        
        self._input_form.render(self._parent)

    def _update_gc(self) -> None:
        """ Commits the current form value updating the selected general contractor. """
        selected_gc = dpg.get_item_user_data(self._selected_list_item)
        user_input = self._input_form.get_value()

        if user_input != selected_gc["name"]:
            self._db.update_gc(selected_gc["id"], user_input)
            selected_gc["name"] = user_input
            dpg.set_item_user_data(self._selected_list_item, selected_gc)
            dpg.set_item_label(self._selected_list_item, user_input)
            self._return_to_gc_manager()

    def _delete_btn_handler(self):
        dpg.set_item_label(self._parent, "Confirm Delete")
        dpg.delete_item(self._parent, children_only=True)
        gc_name = dpg.get_item_user_data(self._selected_list_item)["name"]
        self._confirmation_form.set_prompt(f"Are you sure you want to delete GC '{gc_name}'?")
        self._confirmation_form.set_confirm_callback(self._delete_gc)
        self._confirmation_form.render(self._parent)

    def _delete_gc(self):
        selected_gc = dpg.get_item_user_data(self._selected_list_item)
        self._db.delete_gen_contractor(selected_gc["id"])
        for idx, gc in enumerate(self._gc_list):
            if selected_gc["id"] == gc["id"]:
                self._gc_list.pop(idx)
                break
        self._update_gc_selectables()
        self._return_to_gc_manager()

    def _update_gc_selectables(self):
        self._gc_list.sort(key=lambda gc : gc["name"])
        dpg.delete_item(self._selectables_container, children_only=True)
        for gc in self._gc_list:
            dpg.add_selectable(
                label=gc["name"],
                parent=self._selectables_container,
                callback=self._gc_selectable_handler,
                user_data=gc
            )

    def _return_to_gc_manager(self) -> None:
        """ 
            To be passed to the add/edit/delete forms as a handler
            when the user completes or cancels any operation.
        """
        dpg.set_item_label(self._parent, "GC Manager")
        dpg.delete_item(self._parent, children_only=True)
        self.render(self._parent)

    def _sort_gcs(self):
        pass

    def _gc_selectable_handler(self, sender): 
        list_item_selected = dpg.get_value(sender)
        
        if list_item_selected:
            self._selected_list_item = sender
            dpg.enable_item(self._update_gc_btn)
            dpg.enable_item(self._delete_gc_btn)
        else:
            self._selected_list_item = None
            dpg.disable_item(self._update_gc_btn)
            dpg.disable_item(self._delete_gc_btn)

        selectables = dpg.get_item_children(self._selectables_container)[1]
        for item in selectables:
            if item != sender:
                dpg.set_value(item, False)
        

    def clear(self):
        """ Resets the GC Manager form to it's default state, no items selected. """
        selectables = dpg.get_item_children(self._selectables_container)[1]
        for item in selectables:
            dpg.set_value(item, False)
        self._selected_list_item = None
        dpg.disable_item(self._update_gc_btn)
        dpg.disable_item(self._delete_gc_btn)

    def render(self, parent):
        self._parent = parent
        dpg.push_container_stack(self._parent)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()

    # ProjectForm.render(self._parent)
    # x = int((dpg.get_viewport_width()/2) - (self.__width/2))
    # y = int((dpg.get_viewport_height()/2) - (self.__height/2))
    # dpg.set_item_pos(self.__id, [x, y])
