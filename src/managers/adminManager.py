from src.entities.AuthorEntity import AuthorEntity
from src.entities.CollectionEntity import CollectionEntity
from src.entities.CategoryEntity import CategoryEntity
from src.entities.PublisherEntity import PublisherEntity
from src.entities.RoleEntity import RoleEntity

class AdminManager:
    def __init__(self, adminRepo):
        self.adminRepo = adminRepo
        
    def get_authors(self):
        #return self.adminRepo.get_all_authors()
        pass
    def create_author(self, name: str):
        author = AuthorEntity(name=name)
        author_id =self.adminRepo.create_author(author)
        if author_id == None:
            return None
        else:
            author.id = author_id
            return author
        
    def create_collec(self, name: str):
        collection = CollectionEntity(name=name)
        collec_id =self.adminRepo.create_collec(collection)
        if collec_id == None:
            return None
        else:
            collection.id = collec_id
            return collection
        
    def create_cat(self, name: str):
        category = CategoryEntity(name=name)
        cat_id =self.adminRepo.create_cat(category)
        if cat_id == None:
            return None
        else:
            category.id = cat_id
            return category
        
    def create_pub(self, name: str):
        publisher = PublisherEntity(name=name)
        pub_id =self.adminRepo.create_pub(publisher)
        if pub_id == None:
            return None
        else:
            publisher.id = pub_id
            return publisher
        
    def create_role(self, name: str):
        role = RoleEntity(name=name)
        role_id =self.adminRepo.create_role(role)
        if role_id == None:
            return None
        else:
            role.id = role_id
            return role