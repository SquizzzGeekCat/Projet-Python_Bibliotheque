import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QStackedWidget
import bcrypt


class LoginPage(QWidget):
    def __init__(self, switch_window):
        super().__init__()
        self.switch_window = switch_window
        self.initUI()

    def initUI(self):
        # Créer une mise en page verticale
        layout = QVBoxLayout()
        

        # Créer des labels et des champs d'entrée
        self.label1 = QLabel('Email:')
        self.input1 = QLineEdit()
        self.label2 = QLabel('Mot de passe:')
        self.input2 = QLineEdit()
        self.input2.setEchoMode(QLineEdit.Password)

        # Créer un bouton
        self.button = QPushButton('Connexion')
        self.button.clicked.connect(self.on_button_click)

        # Ajouter les widgets à la mise en page
        layout.addWidget(self.label1)
        layout.addWidget(self.input1)
        layout.addWidget(self.label2)
        layout.addWidget(self.input2)
        layout.addWidget(self.button)

        # Définir la mise en page de la fenêtre
        self.setLayout(layout)
        

    def on_button_click(self):
        # Récupérer les valeurs des champs d'entrée
        email = self.input1.text()
        # Récupérer les valeurs des champs d'entrée
        password = self.input2.text()
        has_password = self.hash_password(password)
        # Afficher les valeurs dans la console
        print(f'Email: {email}, Mdp: {has_password}')

        # Rediriger vers la deuxième page
        self.switch_window()
    def hash_password(self, password):
        # Hacher le mot de passe
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # return le password hasher
        return self.hashed_password
        
class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Créer une mise en page verticale
        layout = QVBoxLayout()
        

        # Créer un label
        self.label = QLabel('Bienvenue sur la page d\'accueil!')

        # Ajouter le label à la mise en page
        layout.addWidget(self.label)
        

        # Créer un champ de recherche
        self.search_label = QLabel('Recherche:')
        self.search_input = QLineEdit()

        # Créer un bouton de recherche
        self.search_button = QPushButton('Rechercher')
        self.search_button.clicked.connect(self.on_search_click)

        # Ajouter les widgets à la mise en page
        layout.addWidget(self.search_label)
        layout.addWidget(self.search_input)
        layout.addWidget(self.search_button)

        # Définir la mise en page de la fenêtre
        self.setLayout(layout)

    def on_search_click(self):
        # Récupérer la valeur du champ de recherche
        search_query = self.search_input.text()

        # Afficher la valeur dans la console
        print(f'Recherche: {search_query}')


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        self.setGeometry(500, 500, 500, 500)

    def initUI(self):
        # Créer un QStackedWidget pour gérer les pages
        self.stacked_widget = QStackedWidget()

        # Créer les pages
        self.login_page = LoginPage(self.switch_to_home_page)
        self.home_page = HomePage()

        # Ajouter les pages au QStackedWidget
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.home_page)

        # Définir la mise en page de la fenêtre
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

        # Définir le titre et la taille de la fenêtre
        self.setWindowTitle('Mon Application PyQt')
        

    def switch_to_home_page(self):
        self.stacked_widget.setCurrentWidget(self.home_page)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
