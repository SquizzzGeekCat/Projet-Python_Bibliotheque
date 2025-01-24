class AuthorEntity:
    def __init__(self,name, id_autor = None ):
        self.id_autor = id_autor
        self.name = name
        
    def __str__(self):
        return f"this autor name is {self.name}"