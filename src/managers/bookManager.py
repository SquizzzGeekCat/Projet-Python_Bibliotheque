

class BookManager:
    def __init__(self, repo):
        self.repository = repo
        
    def get_books_by_name(self, book_name):
        return self.repository.select_books_by_title(book_name)