import dearpygui.dearpygui as dpg
from Models.App import App

def set_modal_label(label:str):
    dpg.set_item_label(App.modal.value, label)

def clear_modal():
    dpg.delete_item(App.modal.value, children_only=True)

def show_modal():
    dpg.show_item(App.modal.value)