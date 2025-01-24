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
        user = UserEntity(
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["email"],
                password=data["password"],
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
        