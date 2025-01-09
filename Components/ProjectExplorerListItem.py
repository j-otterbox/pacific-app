import dearpygui.dearpygui as dpg

# info needed to create an instance of the class:
# project name
# gc

# sample status for the project in 4 possible states
# - ordered from vendor 
# - delivered to PC 
# - shipped to GC
# - approved by GC 

# pass list of statuses in no particular order for ALL specs
# pass list of spec data

# prduct data status
# - product data gathered

class ProjectExplorerListItem:

    def __init__(self, project_name:str, gc:str, sample_statuses:list, product_data_status:list):

        with dpg.staging_container() as self._staging_container_id:
            with dpg.collapsing_header(label="GC - Project Name"):
                with dpg.group(horizontal=True):
                    dpg.add_button(label="Open", small=True)
                    dpg.add_button(label="Delete", small=True)
                    with dpg.popup(dpg.last_item(), modal=True, mousebutton=dpg.mvMouseButton_Left):
                        dpg.add_text("Please confirm you want to delete project [PROJECT NAME].")
                        with dpg.group(horizontal=True, indent=144):
                            dpg.add_button(label="Yes", width=50)
                            dpg.add_button(label="No", width=50)
                        # dpg.add_separator()
                        # dpg.add_checkbox(label="Don't ask me next time")

                dpg.add_separator()
                dpg.add_text("Samples")
                dpg.add_progress_bar(label="Progress Bar", width=-1, default_value=1, overlay="100% Ordered from Vendors")
                dpg.add_progress_bar(label="Progress Bar", width=-1, default_value=0.78, overlay="78% Delivered to PC")
                dpg.add_progress_bar(label="Progress Bar", width=-1, default_value=0.78, overlay="78% Shipped to GC")
                dpg.add_progress_bar(label="Progress Bar", width=-1, default_value=0.56, overlay="56% Approved by GC")

                dpg.add_text("Product Data")
                dpg.add_progress_bar(label="Progress Bar", width=-1, default_value=0.78, overlay="78% Product Data Gathered")

    def _render_view(self):
        dpg.unstage(self._staging_container_id)