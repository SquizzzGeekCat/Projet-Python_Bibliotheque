class Author:
    def __init__(self,id_autor, name):
        self.id_autor = id_autor
        self.name = name
        
    def __str__(self):
        return f"this autor name is {self.name}"