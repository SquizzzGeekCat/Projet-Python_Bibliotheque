class Address:
    def __init__(self,nbStreet, street, city, state, zip_code):
        self.nbStreet = nbStreet
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        
    def __str__(self):
        return f'{self.nbStreet} {self.street}, {self.city}, {self.state} {self.zip_code}'