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
    def set_title(title:str):
        dpg.set_item_label(c.MODAL, title)

    @staticmethod
    def set_content(stage:int|str):
        dpg.push_container_stack(c.MODAL)
        dpg.unstage(stage)
        dpg.pop_container_stack()

    @staticmethod
    def clear(self):
        dpg.delete_item(c.MODAL, children_only=True)