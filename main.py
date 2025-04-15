
import  dearpygui.dearpygui as dpg
from App import App

if __name__ == "__main__":
    app = App()
    app.init_database()
    app.render_primary_window()
    app.render_login()
    app.start_render_loop()