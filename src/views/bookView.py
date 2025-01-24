from datetime import datetime
from src.entities.BookEntity import BookEntity
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QTableWidgetItem, QTableWidget


class BookView(QWidget):
    def __init__(self):
        super().__init__()
        

    def initUI(self):
        layout = QVBoxLayout()
        
        self.label = QLabel('recherche')
        self.input = QLineEdit()
        # Créer un bouton
        self.search_button = QPushButton('voir les livres')
        
        
        # Configurer le tableau
        self.table_results = QTableWidget(self)
        self.table_results.setColumnCount(7)
        self.table_results.setHorizontalHeaderLabels(['Titre', 'Publier le', 'ISBN','Auteur', 'Editeur','Collection', 'Categorie'])
        
        # Ajouter les widgets à la mise en page
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.table_results)
        self.setLayout(layout)
        
        self.setFixedSize(775, 500)
    def get_title(self):
        # Récupérer la valeur du champ de recherche
        search_query = self.input.text()
        return search_query if search_query else None
        
    def show_books(self, books:list[BookEntity]):
        self.table_results.setRowCount(len(books)-1)
        for book in books:
            row_position = self.table_results.rowCount()
            self.table_results.insertRow(row_position)
            self.table_results.setItem(row_position, 0, QTableWidgetItem(book.title))
            self.table_results.setItem(row_position, 1, QTableWidgetItem(book.publication_date.strftime('%d/%m/%Y')))
            self.table_results.setItem(row_position, 2, QTableWidgetItem(book.ISBN))
            self.table_results.setItem(row_position, 3, QTableWidgetItem(book.authors.name))
            self.table_results.setItem(row_position, 4, QTableWidgetItem(book.publisher.name))
            self.table_results.setItem(row_position, 5, QTableWidgetItem(book.collection.name))
            self.table_results.setItem(row_position, 6, QTableWidgetItem(book.category.name))
            
            
    def connect_btn(self, controller):
        self.initUI()
        self.search_button.clicked.connect(controller.get_books_by_name)
        
        