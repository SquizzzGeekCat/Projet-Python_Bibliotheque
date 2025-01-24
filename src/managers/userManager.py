import bcrypt
from src.entities.UserEntity import UserEntity

class UserManager:
    def __init__(self, repo):
        self.repo = repo
        
    # def authenticate_user(self, username, password):
    #     user = self.repo.get_user_by_username(username)
    #     if user is None:
    #         return None
    #     if user.password == password:
    #         return user
    #     return None
    
    # def get_user_by_id(self, user_id):
    #     return self.repo.get_user_by_id(user_id)
    
    def create_user(self, data):
        password = data["password"]
        # Hasher le mot de passe
        hashed_password = self.hash_password(password)
        user = UserEntity(
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["email"],
                password=hashed_password,
                pseudo=data["pseudo"],
                date_birth=data["birth_date"],
                statut=data["statut"],
                #role=data["role"]  # RoleEntity(id=data["role"]["id"], name=data["role"]["name"])
            )
        user_id = self.repo.create_user(user)
        if user_id == None:
            return None
        else:
            user.id_person = user_id
            return user
    
    def login(self, data:dict):
        password = data["password"]
        password = self.hash_password(password)
        print(password)
        return self.repo.login(data)
    
    
    
    
    
    
    
    
    
    
    # Hasher le mot de passe
    def hash_password(self, password: str) -> bytes:
        # Encoder le mot de passe en bytes
        password_bytes = password.encode('utf-8')
        # Générer un sel
        salt = bcrypt.gensalt()
        # Hasher le mot de passe avec le sel
        hashed = bcrypt.hashpw(password_bytes, salt)
        return hashed