from Modules.Database import Database

class ProjectFormModel:
    def __init__(self):
        pass

    def create_project(self, form_data:dict) -> dict:
        db = Database()
        resp = db.create_project(form_data) 
        return resp

    def validate(self, form_data:dict) -> bool:
        for value in form_data.values():
            if value == "": return False
        return True