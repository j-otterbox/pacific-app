import dearpygui.dearpygui as dpg
from enum import StrEnum

class named_items(StrEnum):
    primary_window = "primary_window"
    content_window = "content_window"
    project_list = "project_list"
    login_view = "login_view"
    pacsee_logo = "pac_c_logo"

def clear_content_window():
    dpg.delete_item(named_items.content_window.value, children_only=True)