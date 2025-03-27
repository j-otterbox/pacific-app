import dearpygui.dearpygui as dpg
from Database import Database
from collections.abc import Callable
from Components.InputTextForm import InputTextForm
from Components.ConfirmationForm import ConfirmationForm

class GCManagerForm:
    def __init__(self, back_btn_callback: Callable=None):
        self._db = Database()
        self._input_form = InputTextForm(input_label="Name", cancel_btn_callback=self._cancel_btn_handler)
        self._confirmation_form = ConfirmationForm()

        with dpg.stage() as self._stage_id:
            with dpg.group(horizontal=True):
                with dpg.child_window(width=240, height=200) as self._gc_list:
                    for gc in self._db.get_all_gcs():
                        dpg.add_selectable(label=gc["name"], user_data=gc, callback=self._gc_list_select_handler)

                with dpg.child_window(border=False, height=200):
                    self._add_gc_btn = dpg.add_button(label="Add", callback=self._add_gc_btn_handler, width=55)
                    self._update_gc_btn = dpg.add_button(label="Edit", callback=self._update_gc_btn_handler, enabled=False, width=55)
                    self._delete_gc_btn = dpg.add_button(label="Delete", enabled=False, width=55)
                    if back_btn_callback is not None:
                        self._back_btn = dpg.add_button(label="Back", callback=back_btn_callback, width=55)

    def _add_gc_btn_handler(self):
        dpg.set_item_label(self._parent, "Add New GC")
        dpg.delete_item(self._parent, children_only=True)
        self._input_form.set_save_btn_callback(self._create_gc)
        self._input_form.render(self._parent)

    def _create_gc(self):
        new_value = self._input_form.get_value()
        print(new_value)

    def _update_gc_btn_handler(self) -> None:
        """ 
            Handler for the GC Manager edit button which opens another form 
            and preloads the name of the currently selected general contractor.
        """
        dpg.set_item_label(self._parent, "Edit GC")
        dpg.delete_item(self._parent, children_only=True)
        self._input_form.set_save_btn_callback(self._update_gc)
        gc_name = dpg.get_item_user_data(self._selected_list_item)["name"]
        self._input_form.set_value(gc_name)        
        self._input_form.render(self._parent)

    def _update_gc(self) -> None:
        """
            
        """
        current_value = dpg.get_item_user_data(self._selected_list_item)["name"]
        new_value = self._input_form.get_value()
        print(current_value, new_value)

    def _cancel_btn_handler(self) -> None:
        """ 
            Input form cancel button handler on Add/Edit GC click 
        """
        dpg.set_item_label(self._parent, "GC Manager")
        dpg.delete_item(self._parent, children_only=True)
        self.render(self._parent)

    def _gc_list_select_handler(self, sender): 
        list_item_selected = dpg.get_value(sender)
        
        if list_item_selected:
            self._selected_list_item = sender
            dpg.enable_item(self._update_gc_btn)
            dpg.enable_item(self._delete_gc_btn)
        else:
            self._selected_list_item = None
            dpg.disable_item(self._update_gc_btn)
            dpg.disable_item(self._delete_gc_btn)

        items = dpg.get_item_children(self._gc_list)[1]
        for item in items:
            if item != sender:
                dpg.set_value(item, False)

    def render(self, parent):
        self._parent = parent
        dpg.push_container_stack(self._parent)
        dpg.unstage(self._stage_id)
        dpg.pop_container_stack()

    # ProjectForm.render(self._parent)
    # x = int((dpg.get_viewport_width()/2) - (self.__width/2))
    # y = int((dpg.get_viewport_height()/2) - (self.__height/2))
    # dpg.set_item_pos(self.__id, [x, y])
