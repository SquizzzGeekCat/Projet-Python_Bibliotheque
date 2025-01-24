class CollectionEntity:
    def __init__(self,name, id_collection=None):
        self.id_collection = id_collection
        self.name = name
        
    def __str__(self):
        return f'Collection({self.id_collection}, {self.name})'