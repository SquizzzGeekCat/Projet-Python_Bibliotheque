
import mysql.connector

from mysql.connector import Error
from src.entities.BookEntity import BookEntity
class BookRepository:
    def __init__(self):
        try:
            self.connexion = mysql.connector.connect(
                host="localhost",          
                user="userlibrary",   
                password="qazwsx00",
                database="librarypython"
            )
            if self.connection.is_connected():
                print("Connexion à la base de données réussie")
            else :
                print("Connexion à la base de données échouée")
        except mysql.connector.Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
            self.connection = None
            

    def select_books_by_title(self,title):
        query = "SELECT * FROM book WHERE Title = %s"
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(query, (title))
            books = cursor.fetchall()
            return [BookEntity(
                book["title"],
                book["publication_date"],
                book["isbn"],
                book["publisher"],
                book["collection"],
                book["category"]) for book in books]
        except Error as e:
            print(f"Erreur lors de la récupération des livres : {e}")
            return []

    