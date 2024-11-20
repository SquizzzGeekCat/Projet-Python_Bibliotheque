class Book:
    def __init__(self, title, author, publication_date, ISBN, publisher, categorie, genre):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.ISBN = ISBN
        self.publisher = publisher
        self.categorie = categorie
        self.genre = genre
        
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPublication Date: {self.publication_date}\nISBN: {self.ISBN}\nPublisher: {self.publisher}\nCategory: {self.category}\nGenre: {self.genre}\n"
    