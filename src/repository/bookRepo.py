
import mysql.connector

from mysql.connector import Error
from src.entities.BookEntity import BookEntity
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
        query = "SELECT * FROM book WHERE Title LIKE %s"
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(query, ('%' + titleInput + '%',))
            books = cursor.fetchall()
            return [BookEntity(
                    id_book = book["Id_Book"],
                    title = book["Title"],
                    publication_date = book["Publich_at"],
                    ISBN = book["ISBN"],
                    publisher = book["Id_Publisher"],
                    collection = book["Id_Collection"],
                    category = book["Id_Category"],
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