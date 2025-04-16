
from os.path import exists
from dotenv import get_key
if not exists(get_key(".env", "DATABASE_NAME")):
    from Modules.Database import init_database
    init_database()
from Modules.App import App

if __name__ == "__main__":
    app = App(title="Pacific Carpets LLC")
    app.render_primary_window()
    app.render_login()
    app.start_render_loop()