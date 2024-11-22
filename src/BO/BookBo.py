from CategorieBo import Categorie
from GenreBo import Genre
from AutorBo import Autor

class Book:
    def __init__(self,id_book, title, author:Autor, publication_date, ISBN, publisher, categorie:Categorie, genre: Genre, reserved=False, disponible=True, date_retour_estimer=None):
        self.id_book = id_book
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.ISBN = ISBN
        self.publisher = publisher
        self.categorie = categorie
        self.genre = genre
        self.reserved = reserved
        self.disponible = disponible
        self.date_retour_estimer = date_retour_estimer
        
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPublication Date: {self.publication_date}\nISBN: {self.ISBN}\nPublisher: {self.publisher}\nCategory: {self.category}\nGenre: {self.genre}\n"
    