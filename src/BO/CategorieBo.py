class Categorie:
    def __init__(self, id_categorie, libelle):
        self.id_categorie = id_categorie
        self.libelle = libelle
        
    def __str__(self):
        return f'Categorie({self.id_categorie}, {self.libelle})'