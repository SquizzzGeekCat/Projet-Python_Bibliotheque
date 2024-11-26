class Category:
    def __init__(self, id_category, libelle):
        self.id_categorie = id_category
        self.libelle = libelle
        
    def __str__(self):
        return f'Categorie({self.id_category}, {self.libelle})'