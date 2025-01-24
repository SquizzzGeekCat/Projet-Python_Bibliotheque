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