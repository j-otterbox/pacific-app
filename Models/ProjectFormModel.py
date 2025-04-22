from Modules.Database import Database

class ProjectFormModel:
    def __init__(self):
        self._db = Database()

    def get_GCs(self, names_only:bool=False):
        gen_contractors = self._db.get_all_GCs()
        if names_only:
            for idx, gen_contractor  in enumerate(gen_contractors):
                gen_contractors[idx] = gen_contractor["name"]
        return gen_contractors

    def get_PMs(self, names_only:bool=False):
        proj_managers = self._db.get_all_PMs()
        if names_only:
            for idx, proj_manager in enumerate(proj_managers):
                proj_managers[idx] = proj_manager["name"]
        return proj_managers 

    def create_project(self, form_data:dict) -> dict:
        resp = self._db.create_project(form_data) 
        return resp

    def validate(self, form_data:dict) -> bool:
        for value in form_data.values():
            if value == "": return False
        return True