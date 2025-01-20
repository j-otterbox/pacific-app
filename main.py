import dearpygui.dearpygui as dpg
from Views.Login import Login
from Views.Dashboard import Dashboard

def load_assets():
    width, height, channels, data = dpg.load_image("Assets/pac_c_logo.png")

    with dpg.texture_registry():
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="pac_c_logo")

dpg.create_context()
dpg.create_viewport(title='Pacific Carpets', width=405, height=200, resizable=False)
load_assets()

with dpg.window(tag="primary_window"):
    Login().render_view()

dpg.set_primary_window("primary_window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

# ==== END MAIN ====