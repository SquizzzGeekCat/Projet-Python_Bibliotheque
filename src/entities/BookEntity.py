from src.entities.CategoryBo import Category
from src.entities.AuthorBo import Author
from src.entities.CollectionBo import Collection
from src.entities.PublisherBo import Publisher

class BookEntity:
    def __init__(self,id_book, title,  publication_date, ISBN,authors=None, publisher:Publisher=None,collection:Collection=None, category:Category=None, adult_only=False):
        # les int
        self.id_book = id_book
        # les strings
        self.title = title
        self.ISBN = ISBN
        # les booelan
        self.adult_only = adult_only
        # les dates
        self.publication_date = publication_date
        # les entites
        self.publisher = publisher
        self.authors = authors
        self.collection = collection
        self.category = category
        
        
        
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPublication Date: {self.publication_date}\nISBN: {self.ISBN}\nPublisher: {self.publisher}\nCategory: {self.category}\n"
    