from src.entities.UserEntity import UserEntity

class UserController:
    def __init__(self, view, manager):
        self.view = view
        self.manager =manager
        
        self.view.connect_btn(self)
        
    def create_user(self):
        data = self.view.get_user_data()
        if data is not None:
            user = self.manager.create_user(data)
            if user is not None:
                message = f"Nouvel utilisateur numero : {user.id_person} nom: {user.first_name} créé avec succès!"
                self.view.showMessage(message)
            else:
                message = "Erreur lors de la création de l'utilisateur"
                self.view.showMessage(message)
        else: 
            message = "Veuillez remplir tous les champs obligatoires"
            return self.view.showMessage(message)
        
    def login(self):
        email = self.view.get_email()
        password = self.view.get_pass()
        data ={"email" : email, "password" : password}
        user = self.manager.login(data)
        if user:
            if user.role == "user":
                message = f"Bienvenue {user.first_name} !"
                self.view.redirectToUserDashbord(user.pseudo,message)
            else:
                message = f"Bienvenue Administrateur!"
                self.view.redirectToAdminDashbord(user.pseudo,message)
        else:
            message = "Email ou mot de passe incorrect"
            self.view.showMessage(message)