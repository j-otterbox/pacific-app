import dearpygui.dearpygui as dpg

class ProjectExplorerListItem:

    def __init__(self, item_data:dict):
        self._name = item_data["name"]
        self._gc = item_data["gc"]
        self._ordered = item_data["ordered"]
        self._received = item_data["received"]
        self._shipped = item_data["shipped"]
        self._approved = item_data["approved"]
        self._data_gathered = item_data["data_gathered"]

        with dpg.stage() as self._staging_container_id:
            with dpg.collapsing_header(label=f"{self._gc} - {self._name}") as self._collapsing_header_id:
                with dpg.group(horizontal=True):
                    dpg.add_button(label="Open", small=True, callback=self._open_project)
                    dpg.add_button(label="Delete", small=True)
                    with dpg.popup(dpg.last_item(), modal=True, mousebutton=dpg.mvMouseButton_Left) as self._confirmation_modal_id:
                        dpg.add_text(f"Please confirm you want to delete project '{self._name}'.")
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

    def _open_project(self):
        pass
        # open project view

    def _delete_project(self):
        dpg.delete_item(self._collapsing_header_id) # deletes ui item
        # TODO: delete project from database
        dpg.hide_item(self._confirmation_modal_id) # hide modal

    def render(self):
        dpg.unstage(self._staging_container_id)