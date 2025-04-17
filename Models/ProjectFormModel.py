from Modules.Database import Database

class ProjectFormModel:
    def __init__(self):
        self._db = Database()

    def get_proj_managers(self, names_only:bool=False):
        proj_managers = self._db.get_all_proj_managers()
        if names_only:
            for idx, proj_manager in enumerate(proj_managers):
                proj_managers[idx] = proj_manager["name"]
        return proj_managers 

    def get_gen_contractors(self, names_only:bool=False):
        gen_contractors = self._db.get_all_gen_contractors()
        if names_only:
            for idx, gen_contractor  in enumerate(gen_contractors):
                gen_contractors[idx] = gen_contractor["name"]
        return gen_contractors

    def create_project(self, form_data:dict) -> dict:
        resp = self._db.create_project(form_data) 
        return resp

    def validate(self, form_data:dict) -> bool:
        for value in form_data.values():
            if value == "": return False
        return True