import sys
from PyQt5.QtWidgets import QWidget,QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from src.entities.AuthorEntity import AuthorEntity

class AdminView(QWidget):
    def __init__(self):
        super().__init__()
        

    def initUI(self):
        layout = QVBoxLayout()
        
        #params de la fenetre
        #self.setWindowTitle('vue admin')
        #self.setWindowIcon(QtGui.QIcon('icon.png'))
        
        #create author
        self.label_author = QLabel('nom auteur')
        self.input_author = QLineEdit()
        self.create_btn_author = QPushButton('crée auteur')
        #create collection
        self.label_collec = QLabel('nom collection')
        self.input_collec = QLineEdit()
        self.create_btn_collec = QPushButton('crée collection')
        
        # create category
        self.label_cat = QLabel('nom Catégorie')
        self.input_cat = QLineEdit()
        self.create_btn_cat = QPushButton('crée catégorie')
        
        # create publisher
        self.label_pub = QLabel("nom d'éditeur")
        self.input_pub = QLineEdit()
        self.create_btn_pub = QPushButton("crée Éditeur")
        
        # create role
        self.label_role = QLabel('nom du Role')
        self.input_role = QLineEdit()
        self.create_btn_role = QPushButton('crée Role')
        
        
         # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_author)
        layout.addWidget(self.input_author)
        layout.addWidget(self.create_btn_author)
        layout.addWidget(self.label_collec)
        layout.addWidget(self.input_collec)
        layout.addWidget(self.create_btn_collec)
        layout.addWidget(self.label_cat)
        layout.addWidget(self.input_cat)
        layout.addWidget(self.create_btn_cat)
        layout.addWidget(self.label_pub)
        layout.addWidget(self.input_pub)
        layout.addWidget(self.create_btn_pub)
        layout.addWidget(self.label_role)
        layout.addWidget(self.input_role)
        layout.addWidget(self.create_btn_role)

        # Conteneur central
        self.setLayout(layout)
    def getAuthorName(self):
        newAuthor = self.input_author.text()
        return newAuthor if newAuthor else None
    
    def getCollecName(self):
        newCollec = self.input_collec.text()
        return newCollec if newCollec else None
    
    def getCatName(self):
        newCat = self.input_cat.text()
        return newCat if newCat else None
    
    def getPubName(self):
        newPub = self.input_pub.text()
        return newPub if newPub else None
    
    def getRoleName(self):
        newRole = self.input_role.text()
        return newRole if newRole else None
    
    
    def showMessage(self, message):
        QMessageBox.information(self, "Jarvis Message", message)
        self.input_author.setText("")
        self.input_collec.setText("")
        self.input_cat.setText("")
        self.input_role.setText("")
        self.input_pub.setText("")
        
    def connect_btn(self, controller):
        self.initUI()
        self.create_btn_author.clicked.connect(controller.create_author)
        self.create_btn_collec.clicked.connect(controller.create_collec)
        self.create_btn_cat.clicked.connect(controller.create_cat)
        self.create_btn_pub.clicked.connect(controller.create_pub)
        self.create_btn_role.clicked.connect(controller.create_role)
    
