
import mysql.connector

from mysql.connector import Error
from src.entities.BookEntity import BookEntity
from entities.AuthorEntity import AuthorEntity
from entities.PublisherEntity import PublisherEntity
from entities.CategoryEntity import CategoryEntity
from entities.CollectionEntity import CollectionEntity
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
            return [BookEntity(
                    id_book = book["Id_Book"],
                    title = book["Title"],
                    publication_date = book["Publiched_at"],
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
        finally:
            cursor.close()
            print("Connexion à la base de données fermée")

    def archived_book(self, id_book, date_archived):
        #TODO: a tester
        query = """UPDATE book SET Archived_at=%s WHERE Id_Book = %s"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (date_archived,id_book))
            self.conn.commit()
            print("Livre archivé avec succès")
        except Error as e:
            print(f"Erreur lors de l'archivage du livre : {e}")
        finally:
            cursor.close()
            print("Connexion à la base de données fermée")
    def create_book(self, book_entity):
        query = """INSERT INTO book
        (`Title`, 
        `Publiched_at`, 
        `ISBN`, 
        `Adult_only`, 
        `Created_at`, 
        `Id_Administrator_creation`, 
        `Id_Publisher`, 
        `Id_Collection`, 
        `Id_Category`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        values = (book_entity.title,book_entity.publiched_at,book_entity.ISBN,book_entity.Adult_only, book_entity.Creates_at,book_entity.Id_Administrator_creation,book_entity.Id_Publisher,book_entity.Id_Collection,book_entity.Id_Category)
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, values)
            self.conn.commit()
            print("Livre créé avec succès")
            return cursor.lastrowid
        except Error as e:
            print(f"Erreur lors de l'ajout du livre : {e}")
            return None
        
    def __del__(self):
        """
        Ferme la connexion à la base de données.
        """
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Connexion à la base de données fermée")