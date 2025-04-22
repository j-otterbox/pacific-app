import dearpygui.dearpygui as dpg
from collections.abc import Callable
import constants as c

class ContentWindow:
    def __init__(self):
        pass

    @staticmethod
    def clear():
        dpg.delete_item(c.CONTENT_WINDOW, children_only=True)

class Modal():
    def __init__(self):
        pass

    @staticmethod
    def get_tag(self):
        return c.MODAL

    @staticmethod
    def show():
        dpg.show_item(c.MODAL)
        
    @staticmethod
    def hide():
        dpg.hide_item(c.MODAL)

    @staticmethod
    def set_title(title:str):
        dpg.set_item_label(c.MODAL, title)

    @staticmethod
    def set_content(stage_id:int|str):
        dpg.push_container_stack(c.MODAL)
        dpg.unstage(stage_id)
        dpg.pop_container_stack()

    @staticmethod
    def clear():
        dpg.delete_item(c.MODAL, children_only=True)

    @staticmethod 
    def delete_on_close(stages:list[int]):
        def on_close():
            dpg.delete_item(c.MODAL, children_only=True)
            for item in stages:
                dpg.delete_item(item)
        dpg.configure_item(c.MODAL, on_close=on_close)