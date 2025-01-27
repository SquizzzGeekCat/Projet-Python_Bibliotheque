
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox

class UserDashboard(QWidget):
    def __init__(self, acceuil_message, pseudo):
        super().__init__()
        self.acceuil_message = acceuil_message
        self.pseudo = pseudo

    def initUI(self):
        layout = QVBoxLayout()
        
        self.label = QLabel(self.acceuil_message)
        layout.addwidget(self.label)
        
        # Définir le layout pour la fenêtre principale
        self.setLayout(layout)

        # Définir les propriétés de la fenêtre
        self.setWindowTitle('User Dashboard')