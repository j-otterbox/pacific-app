
from Database import init_database
from Controllers.AppController import AppController

if __name__ == "__main__":
    init_database()
    app = AppController()
    app.bootstrap()
