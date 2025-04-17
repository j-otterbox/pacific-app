from Modules.Database import Database

class ManagerFormModel:
    def __init__(self):
        self._db = Database()

    def get_PMs(self):
        return self._db.get_all_PMs()

    def get_GCs(self):
        return self._db.get_all_GCs()
    
