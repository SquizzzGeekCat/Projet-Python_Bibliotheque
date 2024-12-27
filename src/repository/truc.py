def select_book_by_author(self,author):
        pass

def select_book_by_category(self,category):
    pass

def select_book_by_publisher(self,publisher):
    pass

def select_book_by_collection(self,collection):
    pass

# create querie
def insert_book(self,book):
    pass

# update queries
def update_book(self,id):
    pass

def update_book_return_date(self,id, return_date):
    pass

# archive queries
def archive_book_by_id(self,id):
    pass
# select type queries
    #
    
    
    [{'Id_Book': 1, 
      'Title': "Harry Potter et l'Ordre du Phénix", 
      'Publich_at': datetime.date(2003, 12, 3), 
      'ISBN': '2-07-055685-9', 'Adult_only': 0, 
      'Create_at': datetime.date(2024, 12, 17), 
      'Archive_at': None, 
      'Id_Administrator_archive': None, 
      'Id_Administrator_creation': 1, 
      'Id_Publisher': 1, 
      'Id_Collection': 1, 
      'Id_Category': 1, 
      'Name_Author': 'J.K Rolling', 
      'Name_collection': 'Wizarding world ', 
      'Name_Category': 'Fantasie', 
      'Name_Publisher': 'Gallimard jeunesse'}, 
     
     {'Id_Book': 4, 
      'Title': 'Orgueil et Préjugés', 
      'Publich_at': datetime.date(2007, 1, 1), 
      'ISBN': '978-2-07-033866-5', 
      'Adult_only': 0, 
      'Create_at': datetime.date(2024, 12, 17), 
      'Archive_at': None, 
      'Id_Administrator_archive': None, 
      'Id_Administrator_creation': 1, 
      'Id_Publisher': 4, 
      'Id_Collection': None, 
      'Id_Category': 3, 
      'Name_Author': 'Jane Austen', 
      'Name_collection': None, 
      'Name_Category': 'Romance', 
      'Name_Publisher': 'Gallimard'}]