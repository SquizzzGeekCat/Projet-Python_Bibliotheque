import sys
from PyQt5.QtWidgets import QApplication
from src.managers.bookManager import BookManager
from src.repository.bookRepo import BookRepository
from src.controllers.bookController import BookController
from src.views.bookView import BookView
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    repo = BookRepository()
    view = BookView()
    manager = BookManager(repo)
    controller = BookController(view, manager)
    
    view.show()

    sys.exit(app.exec_())