from CategoryBo import Category
from AuthorBo import Author
from CollectionBo import Collection
from PublisherBo import Publisher

class Book:
    def __init__(self,id_book, title, authors:list[Author], publication_date, ISBN, publisher:Publisher,collection:Collection, category:Category,created_date, archived_date, id_admin_archive, id_admin_create, reserved=False, disponible=True, adult_only=False):
        # les int
        self.id_book = id_book
        self.id_admin_create = id_admin_create
        self.id_admin_archive = id_admin_archive
        # les strings
        self.title = title
        self.ISBN = ISBN
        # les booelan
        self.adult_only = adult_only
        self.reserved = reserved
        # les dates
        self.publication_date = publication_date
        self.created_date = created_date
        self.archive_date = archived_date
        # les entites
        self.publisher = publisher
        self.authors = authors
        self.collection = collection
        self.category = category
        
        
        
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPublication Date: {self.publication_date}\nISBN: {self.ISBN}\nPublisher: {self.publisher}\nCategory: {self.category}\n"
    