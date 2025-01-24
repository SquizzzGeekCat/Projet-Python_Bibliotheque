from PyQt5.QtWidgets import QWidget,QVBoxLayout,QComboBox, QLineEdit, QPushButton, QLabel, QMessageBox

class AdminCreateUserView(QWidget):
    def __init__(self):
        super().__init__()
        

    def initUI(self):
        layout = QVBoxLayout()
        
        self.label_last_name = QLabel("Nom")
        self.input_last_name = QLineEdit()
        
        self.label_first_name = QLabel("Prénom")
        self.input_first_name = QLineEdit()
        
        self.label_pseudo = QLabel("Pseudo")
        self.input_pseudo = QLineEdit()
        
        self.label_birth_date = QLabel("Date de naissance")
        self.input_birth_date = QLineEdit()
        
        self.label_email = QLabel("Email")
        self.input_email = QLineEdit()
        
        self.label_password = QLabel("Mot de passe")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        
        self.label_confirm_password = QLabel("Confirmation mot de passe")
        self.input_confirm_password = QLineEdit()
        self.input_confirm_password.setEchoMode(QLineEdit.Password)
        
        self.label_statut = QLabel("Statut")
        self.input_statut = QComboBox()
        self.input_statut.addItems(['En attente', 'actif','inactif','bloquer'])
        
        self.create_btn_user = QPushButton("Créer")
        
        layout.addWidget(self.label_last_name)
        layout.addWidget(self.input_last_name)
        
        layout.addWidget(self.label_first_name)
        layout.addWidget(self.input_first_name)
        
        layout.addWidget(self.label_pseudo)
        layout.addWidget(self.input_pseudo)
        
        layout.addWidget(self.label_birth_date)
        layout.addWidget(self.input_birth_date)
        
        layout.addWidget(self.label_email)
        layout.addWidget(self.input_email)
        
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        
        layout.addWidget(self.label_confirm_password)
        layout.addWidget(self.input_confirm_password)
        
        layout.addWidget(self.label_statut)
        layout.addWidget(self.input_statut)
        
        layout.addWidget(self.create_btn_user)
        
        self.setLayout(layout)
        
    def showMessage(self, message):
        QMessageBox.information(self, "Jarvis Message", message)
        
    def get_user_data(self):
        last_name = self.input_last_name.text()
        first_name = self.input_first_name.text()
        pseudo = self.input_pseudo.text()
        birth_date = self.input_birth_date.text()
        email = self.input_email.text()
        password = self.input_password.text()
        confirm_password = self.input_confirm_password.text()
        statut = self.input_statut.currentText()
        
        newUser = {
            'last_name': last_name,
            'first_name': first_name,
            'pseudo': pseudo,
            'birth_date': birth_date,
            'email': email,
            'password': password,
            'confirm_password': confirm_password,
            'statut': statut
        }
        return newUser
        
    def showMessage(self, message):
        QMessageBox.information(self, "Jarvis Message", message)
        self.input_first_name.clear()
        self.input_last_name.clear()
        self.input_pseudo.clear()
        self.input_birth_date.clear()
        self.input_email.clear()
        self.input_password.clear()
        self.input_confirm_password.clear()
        self.input_statut.setCurrentIndex(0)

    def connect_btn(self, controller):
        self.initUI()
        self.create_btn_user.clicked.connect(controller.create_user)