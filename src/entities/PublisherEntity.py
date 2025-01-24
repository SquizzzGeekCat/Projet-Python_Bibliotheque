class PublisherEntity:
    def __init__(self,name, id_publisher=None ):
        self.id_publisher = id_publisher
        self.name = name
        
    def __str__(self):
        return f'Publisher({self.id_publisher}, {self.name})'