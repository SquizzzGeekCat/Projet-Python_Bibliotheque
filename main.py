import sys
from PyQt5.QtWidgets import QApplication

from src.views.loginView import LoginView
from src.controllers.userController import UserController
from src.repository.userRepo import UserRepo
from src.managers.userManager import UserManager

if __name__ == "__main__":
    
     app = QApplication(sys.argv)
     repo = UserRepo()
     manager = UserManager(repo)
     view = LoginView()
     controller = UserController(view,manager)
     view.show()
     sys.exit(app.exec_())


# from src.views.createUserView import AdminCreateUserView
# from src.controllers.userController import UserController
# from src.repository.userRepo import UserRepo
# from src.managers.userManager import UserManager
# if __name__ == "__main__":
    
#      app = QApplication(sys.argv)
#      repo = UserRepo()
#      manager = UserManager(repo)
#      view = AdminCreateUserView()
#      controller = UserController(view,manager)
#      view.show()
#      sys.exit(app.exec_())


### pour creation autour du livre

# from src.repository.adminRepo import AdminRepo
# from src.managers.adminManager import AdminManager
# from src.controllers.adminController import AdminController
# from src.views.adCreateView import AdminView
# if __name__ == "__main__":
    
#     app = QApplication(sys.argv)
#     view = AdminView()
#     repo = AdminRepo()
#     manager = AdminManager(repo)
#     controller = AdminController(view, manager)
#     view.show()
#     sys.exit(app.exec_())
    
### pour affichache livres 
# from src.managers.bookManager import BookManager
# from src.repository.bookRepo import BookRepository
# from src.controllers.bookController import BookController
# from src.views.bookView import BookView
# if __name__ == "__main__":
    
#     app = QApplication(sys.argv)
#     repo = BookRepository()
#     view = BookView()
#     manager = BookManager(repo)
#     controller = BookController(view, manager)
    
#     view.show()

#     sys.exit(app.exec_())
    
