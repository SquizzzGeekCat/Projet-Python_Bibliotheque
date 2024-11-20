class Autor:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.books = []
        
    def __str__(self):
        return f"this autor name is {self.firstName} {self.lastName}"