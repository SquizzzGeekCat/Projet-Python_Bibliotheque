from src.entities.BookEntity import BookEntity
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QTableWidgetItem


class BookView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.initUI()
        self.controller = controller

    def initUI(self):
        layout = QVBoxLayout()
        
        self.label = QLabel('recherche')
        self.input = QLineEdit()
        # Créer un bouton
        self.search_button = QPushButton('voir les livres')
        
        # Configurer le tableau
        self.table_results.setColumnCount(6)
        self.table_results.setHorizontalHeaderLabels(['Titre', 'Publier le', 'ISBN', 'Editeur','Collection', 'Categorie'])
        
        # Ajouter les widgets à la mise en page
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.table_results)
        self.setLayout(layout)
        
    def get_title(self):
        # Récupérer la valeur du champ de recherche
        search_query = self.input.text()
        return str(search_query) if search_query else None
        
    def show_books(self, books:list[BookEntity]):
        self.table_results.setRowCount(len(books))
        for book in books:
            row_position = self.table_results.rowCount()
            self.table_results.insertRow(row_position)
            self.table_results.setItem(row_position, 0, QTableWidgetItem(book.title))
            self.table_results.setItem(row_position, 1, QTableWidgetItem(book.publication_date))
            self.table_results.setItem(row_position, 2, QTableWidgetItem(book.isbn))
            self.table_results.setItem(row_position, 3, QTableWidgetItem(book.publisher))
            self.table_results.setItem(row_position, 4, QTableWidgetItem(book.collection))
            self.table_results.setItem(row_position, 5, QTableWidgetItem(book.category))
            
            
    def connect_btn(self, controller):
        self.search_button.clicked.connect(controller.holdup_books_by_name)