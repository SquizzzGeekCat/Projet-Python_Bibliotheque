
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox

class AdminDashboard(QWidget):
    def __init__(self,pseudo ,acceuil_message ):
        super().__init__()
        self.acceuil_message =acceuil_message
        self.pseudo = pseudo
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.label_message_acceuil = QLabel(self.acceuil_message)
        layout.addWidget(self.label_message_acceuil)
        self.setGeometry(300, 300, 400, 300)
        
        self.setLayout(layout)
        self.setWindowTitle('Tableau de Bord Admin')