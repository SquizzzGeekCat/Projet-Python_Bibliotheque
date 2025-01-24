class AdminController:
    def __init__(self, view, adminManager):
        self.view = view
        self.adminManager = adminManager
        
        #pattern signal ou slot
        self.view.connect_btn(self)
        
    def create_author(self):
        name = self.view.getAuthorName()
        if name:
            author = self.adminManager.create_author(name)
            if author is not None:
                message = f"l'auteur {author.name} a été crée avec succès"
                self.view.showMessage(message)
            else :
                message = "Auteur non créé"
                self.view.showMessage(message)
        
        
    def create_collec(self):
        name = self.view.getCollecName()
        if name:
            collection = self.adminManager.create_collec(name)
            if collection is not None:
                message = f"la collection {collection.name} a été crée avec succès"
                self.view.showMessage(message)
            else :
                message = "collection non créé"
                self.view.showMessage(message)
        
    def create_cat(self):
        name = self.view.getCatName()
        if name:
            category = self.adminManager.create_cat(name)
            if category is not None:
                message = f"la categorie {category.name} a été crée avec succès"
                self.view.showMessage(message)
            else :
                message = "categorie non créé"
                self.view.showMessage(message)
    
    def create_pub(self):
        name = self.view.getPubName()
        if name:
            publisher = self.adminManager.create_pub(name)
            if publisher is not None:
                message = f"l'éditeur {publisher.name} a été crée avec succès"
                self.view.showMessage(message)
            else :
                message = "éditeur non créé"
                self.view.showMessage(message)
                
    def create_role(self):
        name = self.view.getRoleName()
        if name:
            role = self.adminManager.create_role(name)
            if role is not None:
                message = f"le role {role.name} a été crée avec succès"
                self.view.showMessage(message)
            else :
                message = "Role non créé"
                self.view.showMessage(message)
        
        
    def getAuthors(self):
        pass