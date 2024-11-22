class Genre:
    def __init__(self, id_genre, libelle):
        self.id_genre = id_genre
        self.libelle = libelle
        
    def __str__(self):
        return f'Genre({self.id_genre}, {self.libelle})'