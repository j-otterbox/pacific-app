from Modules.Database import Database

class DashboardPageModel:
    def __init__(self):
        self._db = Database()
        self._projects = self._db.get_all_projects()

    def get_projects(self):
        return self._projects
    
    def delete_project(self, id:int):
        self._db.delete_project(id)