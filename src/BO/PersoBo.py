class Person:
    # instance attributes
    def __init__(self, first_name, last_name, pseudo, date_birth, email, password, role, address):
        self.first_name = first_name
        self.last_name = last_name
        self.pseudo = pseudo
        self.date_birth = date_birth
        self.email = email
        self.password = password
        self.role = role
        self.address = address

    # instance method
    def introduced(self):
        return f"Hello, my name is {self.first_name} {self.last_name} and I live in {self.address}"
