import dearpygui.dearpygui as dpg
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
        dpg.delete_item(stage_id)

    @staticmethod
    def clear():
        dpg.delete_item(c.MODAL, children_only=True)