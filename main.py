#import sys
#from PyQt5.QtWidgets import QApplication
#from src.managers.bookManager import BookManager
#from src.repository.bookRepo import BookRepository
#from src.controllers.bookController import BookController
import mysql.connector
from mysql.connector import Error
#from src.views.bookView import BookView
if __name__ == "__main__":
    connection = None
    
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            database="mylibrary",
            user="root",
            password=""
        )
        if connection.is_connected():
            print("Connexion à la base de données réussie")
        else :
            print("Connexion à la base de données échouée")

    except mysql.connector.Error as e:
        print(f"Erreur lors de la connexion à la base de données : {e}")
        connection = None
#app = QApplication(sys.argv)
    #repo = BookRepository()
    #view = BookView()
    #manager = BookManager()
    #controller = BookController(manager, view)
    
    #view.show()

    #sys.exit(app.exec_())