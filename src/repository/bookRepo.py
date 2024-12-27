
import mysql.connector

from mysql.connector import Error
from src.entities.BookEntity import BookEntity
from src.entities.AuthorBo import AuthorEntity
from src.entities.PublisherBo import PublisherEntity
from src.entities.CategoryBo import CategoryEntity
from src.entities.CollectionBo import CollectionEntity
class BookRepository:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                port=3306,
                database="mylibrary",
                user="admin",
                password="qazwsx00"
                )
            if self.conn.is_connected():
                print("Connexion à la base de données réussie")
            else :
                print("Connexion à la base de données échouée")
        except mysql.connector.Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
            self.conn = None
            

    def select_books_by_title(self,titleInput):
        query ="""SELECT book.*,writer.Id_Author, author.Name_Author, collection.Name_collection,category.Name_Category,publisher.Name_Publisher FROM book
            LEFT JOIN writer ON writer.Id_Book = book.Id_Book
            LEFT JOIN author ON author.Id_Author = writer.Id_Author
            LEFT JOIN collection ON collection.Id_Collection = book.Id_Collection
            LEFT JOIN category ON category.Id_Category = book.Id_Category
            LEFT JOIN publisher ON publisher.Id_Publisher = book.Id_Publisher
            WHERE book.Title LIKE %s"""
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(query, ('%' + titleInput + '%',))
            books = cursor.fetchall()
            print(books)
            return [BookEntity(
                    id_book = book["Id_Book"],
                    title = book["Title"],
                    publication_date = book["Publich_at"],
                    ISBN = book["ISBN"],
                    authors = AuthorEntity(book["Id_Author"], book["Name_Author"]),
                    publisher = PublisherEntity(book["Id_Publisher"], book["Name_Publisher"]),
                    collection = CollectionEntity(book["Id_Collection"], book["Name_collection"]),
                    category = CategoryEntity(book["Id_Category"],book["Name_Category"]),
                    adult_only = book["Adult_only"]
                )for book in books]
        except Error as e:
            print(f"Erreur lors de la récupération des livres : {e}")
            return []

    def __del__(self):
        """
        Ferme la connexion à la base de données.
        """
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Connexion à la base de données fermée")