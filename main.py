from Modules.App import App

if __name__ == "__main__":
    app = App(title="Pacific Carpets LLC")
    app.render_primary_window()
    app.render_login()
    app.start_render_loop()