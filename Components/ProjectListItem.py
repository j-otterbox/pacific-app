import dearpygui.dearpygui as dpg

class ProjectListItem:
    def __init__(self, parent:int|str, name="default", gc="default"):
        self.__name = name
        self.__gc = gc
        self._ordered = 0
        self._received = 0
        self._shipped = 0
        self._approved = 0
        self._data_gathered = 0

        with dpg.collapsing_header(label=f"{self.__gc} - {self.__name}", parent=parent) as self.__id:
            with dpg.group(horizontal=True):
                dpg.add_button(label="Open", small=True, callback=self.__open_project)
                dpg.add_button(label="Delete", small=True)
                with dpg.popup(dpg.last_item(), modal=True, mousebutton=dpg.mvMouseButton_Left) as self._confirmation_modal_id:
                    dpg.add_text(f"Please confirm you want to delete project '{self.__name}'.")
                    with dpg.group(horizontal=True, indent=144):
                        dpg.add_button(label="Yes", callback=self._delete_project, width=50)
                        dpg.add_button(label="No", callback=lambda _ : dpg.hide_item(self._confirmation_modal_id), width=50)
                    # dpg.add_separator()
                    # dpg.add_checkbox(label="Don't ask me next time")

            dpg.add_separator()
            dpg.add_text("Samples")
            dpg.add_progress_bar(label="Progress Bar", width=-1, default_value=self._ordered, overlay=f"{int(self._ordered * 100)}% Ordered from Vendors")
            dpg.add_progress_bar(label="Progress Bar", width=-1, default_value=self._received, overlay=f"{int(self._received * 100)}% Received by PC")
            dpg.add_progress_bar(label="Progress Bar", width=-1, default_value=self._shipped, overlay=f"{int(self._shipped * 100)}% Shipped to GC")
            dpg.add_progress_bar(label="Progress Bar", width=-1, default_value=self._approved, overlay=f"{int(self._approved * 100)}% Approved by GC")

            dpg.add_text("Product Data")
            dpg.add_progress_bar(label="Progress Bar", width=-1, default_value=self._data_gathered, overlay=f"{int(self._data_gathered * 100)}% Product Data Gathered")

    def __open_project(self):
        pass
        # open project view

    def _delete_project(self):
        dpg.delete_item(self.__id) # deletes ui item
        # TODO: delete project from database
        dpg.hide_item(self._confirmation_modal_id) # hide modal
