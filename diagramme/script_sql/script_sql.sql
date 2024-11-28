CREATE TABLE Role(
   Id_Role INT AUTO_INCREMENT,
   Role_name VARCHAR(10)  NOT NULL,
   PRIMARY KEY(Id_Role),
   UNIQUE(Role_name)
);

CREATE TABLE Category(
   Id_Category INT AUTO_INCREMENT,
   Name_Category VARCHAR(50)  NOT NULL,
   PRIMARY KEY(Id_Category),
   UNIQUE(Name_Category)
);

CREATE TABLE Author(
   Id_Author INT AUTO_INCREMENT,
   Name VARCHAR(30)  NOT NULL,
   PRIMARY KEY(Id_Author),
   UNIQUE(Name)
);

CREATE TABLE Collection(
   Id_Collection INT AUTO_INCREMENT,
   Name_collection VARCHAR(50) ,
   PRIMARY KEY(Id_Collection),
   UNIQUE(Name_collection)
);

CREATE TABLE Publisher(
   Id_Publisher INT AUTO_INCREMENT,
   Name_Publisher VARCHAR(50)  NOT NULL,
   PRIMARY KEY(Id_Publisher),
   UNIQUE(Name_Publisher)
);

CREATE TABLE User_(
   Id_User INT AUTO_INCREMENT,
   Lastname VARCHAR(40)  NOT NULL,
   Firstname VARCHAR(40)  NOT NULL,
   Pseudo VARCHAR(50)  NOT NULL,
   Email VARCHAR(50)  NOT NULL,
   Password VARCHAR(50)  NOT NULL,
   Born_at DATE NOT NULL,
   Statut Enum("Actif", "Inactif", "en attente") NOT NULL,
   Id_Role INT NOT NULL,
   PRIMARY KEY(Id_User),
   UNIQUE(Pseudo),
   UNIQUE(Email),
   FOREIGN KEY(Id_Role) REFERENCES Role(Id_Role)
);

CREATE TABLE Administrator(
   Id_Administrator INT AUTO_INCREMENT,
   Id_User INT NOT NULL,
   PRIMARY KEY(Id_Administrator),
   UNIQUE(Id_User),
   FOREIGN KEY(Id_User) REFERENCES User_(Id_User)
);

CREATE TABLE Book(
   Id_Book INT AUTO_INCREMENT,
   Title VARCHAR(50)  NOT NULL,
   Publich_at DATE NOT NULL,
   ISBN VARCHAR(50)  NOT NULL,
   Adult_only BOOLEAN,
   Create_at DATE NOT NULL,
   Archive_at DATE,
   Id_Administrator_Archive INT NOT NULL,
   Id_Administrator_Create INT NOT NULL,
   Id_Publisher INT NOT NULL,
   Id_Collection INT NOT NULL,
   Id_Category INT NOT NULL,
   PRIMARY KEY(Id_Book),
   UNIQUE(ISBN),
   FOREIGN KEY(Id_Administrator_Archive) REFERENCES Administrator(Id_Administrator),
   FOREIGN KEY(Id_Administrator_Create) REFERENCES Administrator(Id_Administrator),
   FOREIGN KEY(Id_Publisher) REFERENCES Publisher(Id_Publisher),
   FOREIGN KEY(Id_Collection) REFERENCES Collection(Id_Collection),
   FOREIGN KEY(Id_Category) REFERENCES Category(Id_Category)
);

CREATE TABLE Borrow(
   Id_Borrow INT AUTO_INCREMENT,
   Borrow_date DATE NOT NULL,
   Id_Book INT NOT NULL,
   Id_User INT NOT NULL,
   PRIMARY KEY(Id_Borrow),
   FOREIGN KEY(Id_Book) REFERENCES Book(Id_Book),
   FOREIGN KEY(Id_User) REFERENCES User_(Id_User),
   CONSTRAINT UK_reservation_id UNIQUE(Id_Book, Borrow_date)
);

CREATE TABLE Reservation(
   Id_Reservation INT AUTO_INCREMENT,
   reservation_date DATETIME NOT NULL,
   Id_User INT NOT NULL,
   Id_Book INT NOT NULL,
   PRIMARY KEY(Id_Reservation),
   FOREIGN KEY(Id_User) REFERENCES User_(Id_User),
   FOREIGN KEY(Id_Book) REFERENCES Book(Id_Book),
);

CREATE TABLE Modification(
   Id_Modification INT AUTO_INCREMENT,
   date_modify DATE,
   Id_Administrator INT NOT NULL,
   Id_Book INT NOT NULL,
   PRIMARY KEY(Id_Modification),
   FOREIGN KEY(Id_Administrator) REFERENCES Administrator(Id_Administrator),
   FOREIGN KEY(Id_Book) REFERENCES Book(Id_Book)
);

CREATE TABLE write(
   Id_Book INT,
   Id_Author INT,
   PRIMARY KEY(Id_Book, Id_Author),
   FOREIGN KEY(Id_Book) REFERENCES Book(Id_Book),
   FOREIGN KEY(Id_Author) REFERENCES Author(Id_Author)
);
