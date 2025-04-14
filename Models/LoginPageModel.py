from Database import Database
from hashlib import sha256

class LoginPageModel:
    def __init__(self):
        self._username = ""
    
    def set_username(self, username:str):
        self._username = username
         
    def validate_login(self, username:str, password:str) -> bool:
        db = Database()
        user = db.get_user_by_username(username)
        password_hash = self.convert_to_hash_str(password)
        if user is not None:
            return user["pass_hash"] == password_hash
        return False
    
    def convert_to_hash_str(self, password:str) -> str:
        bytes = bytearray(password, encoding="utf8")
        hash_obj = sha256(bytes)
        return hash_obj.hexdigest()