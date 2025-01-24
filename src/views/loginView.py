import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from src.views.userDashboard import UserDashboard
from src.views.adminDashboard import AdminDashboard

class LoginView(QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        layout = QVBoxLayout()

        # Créer des QLineEdit pour l'email et le mot de passe
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText('Email')
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Mot de passe')
        self.password_input.setEchoMode(QLineEdit.Password)

        # Créer un QPushButton pour se connecter
        self.login_button = QPushButton('Se connecter')

        # Ajouter les widgets au layout
        layout.addWidget(QLabel('Email:'))
        layout.addWidget(self.email_input)
        layout.addWidget(QLabel('Mot de passe:'))
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        # Définir le layout pour la fenêtre principale
        self.setLayout(layout)

        # Définir les propriétés de la fenêtre
        self.setWindowTitle('Connexion')

    def get_pass(self):
        password = self.password_input.text()
        return password
    
    def get_email(self):
        email = self.email_input.text()
        return email
    
    def redirectToUserDashbord(self, pseudo: str, message: str):
        self.user_dashboard = UserDashboard(pseudo, message)
        self.user_dashboard.show()
        self.close()

    def redirectToAdminDashbord(self, pseudo: str, message: str):
        self.admin_dashboard = AdminDashboard(pseudo, message)
        self.admin_dashboard.show()
        self.close()
    
    def connect_btn(self, controller):
        self.initUI()
        self.login_button.clicked.connect(controller.login)    
    

