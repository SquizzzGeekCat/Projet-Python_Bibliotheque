from src.entities.RoleEntity import RoleEntity

class UserEntity:
    def __init__(self, first_name, last_name, pseudo, date_birth, email, password, role, statut="en attente", id_person=None):
        # int
        self.id_person = id_person
        # strings
        self.first_name = first_name
        self.last_name = last_name
        self.pseudo = pseudo
        self.email = email
        self.password = password
        # entity
        self.role = role
        # dates
        self.date_birth = date_birth
        # enum
        self.statut = statut
        
# methodes
    def introduced(self):
        return f"Hello, my name is {self.first_name} {self.last_name}"

