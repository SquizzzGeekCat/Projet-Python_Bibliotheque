class Role:
    def __init__(self,id_role, role_name):
        self.id_role = id_role
        self.role_name = role_name
        
    def __str__(self):
        return f'Role({self.id_role}, {self.role_name})'