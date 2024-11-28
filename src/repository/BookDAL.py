from connexionBDD import db_connexion

# select type queries
def select_all_book():
    conn = db_connexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book")  # Remplace par ta table
    results = cursor.fetchall()
    
    for row in results:
        print(row)
    
    cursor.close()
    conn.close()

def select_book_by_id(id):
    pass

def select_book_by_author(author):
    pass

def select_book_by_category(category):
    pass

def select_book_by_publisher(publisher):
    pass

def select_book_by_collection(collection):
    pass

# create querie
def insert_book(book):
    pass

# update queries
def update_book(id):
    pass

def update_book_return_date(id, return_date):
    pass

# archive queries
def archive_book_by_id(id):
    pass
