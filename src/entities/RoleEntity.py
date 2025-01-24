class RoleEntity:
    def __init__(self,name, id_role=None ):
        self.id_role = id_role
        self.name = name
        
    def __str__(self):
        return f'Role({self.id_role}, {self.name})'