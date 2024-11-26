from RoleBo import Role

class User:
    def __init__(self,id_person, first_name, last_name, pseudo, date_birth, email, password, role: Role, statut="en attente"):
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
        
        
#getter and setter
    @property
    def first_name(self)->str:
        return self.first_name
    @first_name.setter
    def first_name(self, value:str):
        self.first_name = value
        
    @property
    def last_name(self)->str:
        return self.last_name
    @last_name.setter
    def last_name(self, value:str):
        self.last_name = value
        
# methodes
    def introduced(self):
        return f"Hello, my name is {self.first_name} {self.last_name} and I live in {self.address}"

