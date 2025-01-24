class CategoryEntity:
    def __init__(self,name, id_category=None ):
        self.id_categorie = id_category
        self.name = name
        
    def __str__(self):
        return f'Categorie({self.id_category}, {self.name})'