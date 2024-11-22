from AddressBo import Address
from RoleBo import Role

class Person:
    # instance attributes
    def __init__(self,id_person, first_name, last_name, pseudo, date_birth, email, password, role: Role,address:Address, has_reserved = False,  statut="en attente"):
        self.id_person = id_person
        self.first_name = first_name
        self.last_name = last_name
        self.pseudo = pseudo
        self.date_birth = date_birth
        self.email = email
        self.password = password
        self.role = role
        self.address = address
        self.has_reserved = has_reserved
        self.statut = statut

    # instance method
    def introduced(self):
        return f"Hello, my name is {self.first_name} {self.last_name} and I live in {self.address}"
