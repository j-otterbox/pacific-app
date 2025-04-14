
import  dearpygui.dearpygui as dpg
from App import App
# from Database import init_database
# from Controllers.AppController import AppController

if __name__ == "__main__":
    dpg.create_context()
    dpg.create_viewport(title="Pacific Carpets LLC")
    app = App()
    app.render_primary_window()
    app.render_login_page()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()