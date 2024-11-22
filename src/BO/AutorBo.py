class Autor:
    def __init__(self,id_autor, firstName, lastName):
        self.id_autor = id_autor
        self.firstName = firstName
        self.lastName = lastName
        
    def __str__(self):
        return f"this autor name is {self.firstName} {self.lastName}"