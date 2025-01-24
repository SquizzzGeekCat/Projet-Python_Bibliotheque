
class BookController:
    def __init__(self, view, manager):
        self.manager = manager
        self.view = view
        
        #pattern signal ou slot
        self.view.connect_btn(self)
        
    def get_books_by_name(self):
        book_title = self.view.get_title()
        books = self.manager.get_books_by_name(book_title)
        self.view.show_books(books)
