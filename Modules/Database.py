import sqlite3
from time import strftime, gmtime
from os.path import exists
from dotenv import load_dotenv, get_key

load_dotenv()
DATABASE_NAME = get_key(".env", "DATABASE_NAME")

class Database:
    def __init__(self):
        self._conn = sqlite3.connect(DATABASE_NAME)
        self._cursor = self._conn.cursor()

    def create_user(self, username, pass_hash):
        self._cursor.execute("INSERT INTO users (username, pass_hash) VALUES (?, ?)", (username, pass_hash,))
        self._conn.commit()

    def create_PM(self, name) -> dict:
        """ Create a new project mananger under the given name, returns new record on success. """
        resp = self._create_response()
        try:
            self._cursor.execute("INSERT INTO project_managers (name) VALUES (?)", (name))
            query_results = self._cursor.fetchall()
            query_results[0] = self._PM_factory(query_results[0])
            self._conn.commit()
            resp["success"] = True
            resp["data"] = query_results

        except sqlite3.IntegrityError as err:
            resp["success"] = False
            if "UNIQUE constraint failed" in str(err): 
                resp["msg"] = "There is already a PM that goes by this name."
        return resp

    def create_GC(self, name) -> dict:
        """
            Creates a new general contractor under the given name, returns new record on success.
        """
        resp = self._create_response()
        try:
            self._cursor.execute("INSERT INTO general_contractors (name) VALUES (?) RETURNING rowid, *", (name,))
            query_results = self._cursor.fetchall()
            query_results[0] = self._GC_factory(query_results[0])
            self._conn.commit()
            resp["success"] = True
            resp["data"] = query_results
            
        except sqlite3.IntegrityError as err:
            resp["success"] = False
            if "UNIQUE constraint failed" in str(err): 
                resp["msg"] = "There is already a GC that goes by this name."
        return resp

    def create_project(self, payload:dict) -> dict:
        resp = self._create_response()
        try:
            self._cursor.execute("INSERT INTO projects (job_id, pm, gc, name) VALUES (:job_id, :pm, :gc, :name) RETURNING rowid, *", (payload))
            query_results = self._cursor.fetchall()
            query_results[0] = self._project_factory(query_results[0])
            # self._conn.commit()
            resp["success"] = True
            resp["data"] = query_results

        except sqlite3.IntegrityError as err:
            err = str(err)
            resp["success"] = False
            if err == "UNIQUE constraint failed: projects.job_id": 
                resp["msg"] = "job_id conflict"
            elif err == "UNIQUE constraint failed: projects.name":
                resp["msg"] = "name conflict"
        return resp

    def create_spec(self):
        self._cursor.execute()
        self._conn.commit()

    def get_user_by_username(self, username:str):
        resp = self._cursor.execute("SELECT rowid, * FROM users WHERE username=(?)", (username,))
        user = resp.fetchone()
        if user is not None:
            user = self._user_factory(user)
        return user

    def get_all_users(self):
        resp = self._cursor.execute("SELECT rowid, * FROM users")
        user_list = resp.fetchall()
        for idx, user in enumerate(user_list):
            user_list[idx] = self._user_factory(user)
        return user_list

    def get_all_PMs(self):
        resp = self._cursor.execute("SELECT rowid, * FROM project_managers ORDER BY name")
        pm_list = resp.fetchall()
        for idx, pm in enumerate(pm_list):
            pm_list[idx] = self._PM_factory(pm)
        return pm_list

    def get_all_GCs(self):
        resp = self._cursor.execute("SELECT rowid, * FROM general_contractors ORDER BY name")
        gc_list = resp.fetchall()
        for idx, gc in enumerate(gc_list):
            gc_list[idx] = self._GC_factory(gc)
        return gc_list

    def get_all_projects(self):
        resp = self._cursor.execute("SELECT rowid, * FROM projects ORDER BY gc")
        projects_list = resp.fetchall()
        for idx, project in enumerate(projects_list):
            projects_list[idx] = self._project_factory(project)
        return projects_list

    def update_user_pass_hash(self, id, pass_hash):
        self._cursor.execute("UPDATE users SET pass_hash=(?), modified_date=CURRENT_TIMESTAMP WHERE rowid=(?)", (pass_hash, id))
        self._conn.commit()

    def update_PM(self, id, name):
        self._cursor.execute("UPDATE project_managers SET name=(?), modified_date=CURRENT_TIMESTAMP WHERE rowid=(?)", (name, id))
        self._conn.commit()

    def update_GC(self, id:int|str, name:str):
        self._cursor.execute("UPDATE general_contractors SET name=(?), modified_date=CURRENT_TIMESTAMP WHERE rowid=(?)", (name, id))
        self._conn.commit()

    def delete_user(self, id):
        self._cursor.execute("DELETE FROM users WHERE rowid=(?)", (id))
        self._conn.commit()

    def delete_PM(self, id):
        self._cursor.execute("DELETE FROM project_managers WHERE rowid=(?)", (id,))
        self._conn.commit()

    def delete_GC(self, id:int|str):
        self._cursor.execute("DELETE FROM general_contractors WHERE rowid=(?)", (id,))
        self._conn.commit()

    def delete_project(self, id:int|str):
        self._cursor.execute("DELETE FROM projects WHERE rowid=(?)", (id))
        self._conn.commit()

    def _get_current_timestamp(self):
        return strftime("%Y-%m-%d %H:%M:%S", gmtime())

    def _user_factory(self, user:tuple):
        return {
                "id": user[0],
                "username": user[1],
                "pass_hash": user[2],
                "create_date": user[3],
                "modified_date": user[4]
        }

    def _PM_factory(self, pm:tuple):
        return {
            "id": pm[0],
            "name": pm[1],
            "create_date": pm[2],
            "modified_date": pm[3]
        }

    def _GC_factory(self, gc:tuple):
        return {
            "id": gc[0],
            "name": gc[1],
            "create_date": gc[2],
            "modified_date": gc[3]
        }

    def _project_factory(self, project:tuple):
        return {
            "job_id": project[1],
            "pm": project[2],
            "gc": project[3],
            "name": project[4]
        }

    def _create_response(self, success:bool=False, msg:str="", data:list=[]):
        return {
            "success": success,
            "msg": msg,
            "data": data
        }

def init_database():
    """
        Initializes the DB with all required tables and default data 
        if the DB file does not exist in the top-level directory. 
    """
    if not exists(DATABASE_NAME):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        _create_tables(conn)
        _create_admin_user(conn)
        _create_project_managers(conn)
        _create_general_contractors(conn)

        # for testing during development - delete later
        resp = cursor.execute("SELECT name FROM sqlite_master")
        print(resp.fetchall())

        conn.close()
    else:
        print("DB exists, no init needed.")

def _create_tables(conn:sqlite3.Connection):
    cursor = conn.cursor()
    cursor.executescript(
    """
        CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE, pass_hash TEXT, create_date TEXT DEFAULT CURRENT_TIMESTAMP, modified_date TEXT DEFAULT CURRENT_TIMESTAMP);
        CREATE TABLE IF NOT EXISTS project_managers (name TEXT UNIQUE, create_date TEXT DEFAULT CURRENT_TIMESTAMP, modified_date TEXT DEFAULT CURRENT_TIMESTAMP);
        CREATE TABLE IF NOT EXISTS general_contractors (name TEXT UNIQUE, create_date TEXT DEFAULT CURRENT_TIMESTAMP, modified_date TEXT DEFAULT CURRENT_TIMESTAMP);
        CREATE TABLE IF NOT EXISTS projects (job_id TEXT UNIQUE, pm INTEGER, gc INTEGER, name TEXT UNIQUE, create_date TEXT DEFAULT CURRENT_TIMESTAMP, modified_date TEXT DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (pm) REFERENCES project_managers (rowid), FOREIGN KEY (gc) REFERENCES general_contractors (rowid));
        CREATE TABLE IF NOT EXISTS carpet (
            project_id INTEGER,
            scope TEXT,
            location TEXT,
            type TEXT,
            callout TEXT,
            vendor TEXT,
            collection TEXT,
            style TEXT,
            fiber_type TEXT,
            color TEXT,
            length TEXT,
            width TEXT,
            weight TEXT,
            backing TEXT,
            adhesive TEXT,
            samples TEXT,
            specs TEXT,
            maintenance TEXT,
            warranty TEXT,
            FOREIGN KEY (project_id) REFERENCES projects (rowid)
        );
    """)
    # TODO: create table for tile and resilient

def _create_admin_user(conn:sqlite3.Connection):
    cursor = conn.cursor()
    username=get_key(".env", "ADMIN_USERNAME")
    pass_hash = get_key(".env", "ADMIN_PASS_HASH")
    cursor.execute("INSERT INTO users (username, pass_hash) VALUES (?, ?)", (username, pass_hash,))
    conn.commit()

def _create_project_managers(conn:sqlite3.Connection):
    cursor = conn.cursor()
    pm_list = [
        "Clint Walker",
        "Kim Raffee",
        "Jermey Simoneaux",
        "Robert Yula",
        "Rymmy Andre"
    ]
    for name in pm_list:
        cursor.execute("INSERT INTO project_managers (name) VALUES (?)", (name,))
    conn.commit()

def _create_general_contractors(conn:sqlite3.Connection):
    cursor = conn.cursor()
    general_contractors = [
        ("AECOM",),
        ("Alliance Residential",),
        ("Benchmark Contractors",),
        ("Build Group",),
        ("Consolidated Contracting Services",),
        ("Carmel Partners",),
        ("C.W. Driver",),
        ("Fairfield Residential",),
        ("Hanover Company",),
        ("Holland Construction",),
        ("Milender-White",),
        ("Multi-Family Builders",),
        ("R.D. Olson",),
        ("Snyder Langston",),
        ("W.E. O'Neil",),
        ("Westport Construction (WPIC)",)
    ]
    cursor.executemany("INSERT INTO general_contractors (name) VALUES (?)", general_contractors)
    conn.commit()

if __name__ == "__main__":
    pass
    # init_database()
    # db = Database()
    # new_project = {
    #     "job_id": "000001",
    #     "pm": "Lisa Green",
    #     "gc": "W.E.O.",
    #     "name": "Main Street 123"
    # }
    # resp = db.create_project(new_project)
    # print(resp)
    # for key, value in resp.items():
    #     print(key, value)