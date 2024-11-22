CREATE TABLE Role(
   Id_Role INT AUTO_INCREMENT,
   nom VARCHAR(10)  NOT NULL,
   PRIMARY KEY(Id_Role),
   UNIQUE(nom)
);

CREATE TABLE Adresse(
   Id_Adresse INT AUTO_INCREMENT,
   Numero VARCHAR(5)  NOT NULL,
   Rue VARCHAR(50)  NOT NULL,
   Complement VARCHAR(50) ,
   CP INT NOT NULL,
   Ville VARCHAR(30)  NOT NULL,
   PRIMARY KEY(Id_Adresse)
);

CREATE TABLE Genre(
   Id_Genre INT AUTO_INCREMENT,
   Nom VARCHAR(50)  NOT NULL,
   PRIMARY KEY(Id_Genre),
   UNIQUE(Nom)
);

CREATE TABLE Categorie(
   Id_Categorie INT AUTO_INCREMENT,
   Nom VARCHAR(50)  NOT NULL,
   PRIMARY KEY(Id_Categorie),
   UNIQUE(Nom)
);

CREATE TABLE Auteur(
   Id_Auteur INT AUTO_INCREMENT,
   Nom VARCHAR(30)  NOT NULL,
   Prenom VARCHAR(30)  NOT NULL,
   PRIMARY KEY(Id_Auteur)
);

CREATE TABLE Personne(
   ID_Personne INT AUTO_INCREMENT,
   Nom VARCHAR(40)  NOT NULL,
   Prenom VARCHAR(40)  NOT NULL,
   Pseudo VARCHAR(50)  NOT NULL,
   Email VARCHAR(50)  NOT NULL,
   MDP VARCHAR(50)  NOT NULL,
   Date_Naissance DATE NOT NULL,
   had_reserved BOOLEAN NOT NULL,
   statut Enum("Actif", "Inactif", "en attente") NOT NULL,
   Id_Adresse INT NOT NULL,
   Id_Role INT NOT NULL,
   PRIMARY KEY(ID_Personne),
   UNIQUE(Pseudo),
   UNIQUE(Email),
   UNIQUE(MDP),
   FOREIGN KEY(Id_Adresse) REFERENCES Adresse(Id_Adresse),
   FOREIGN KEY(Id_Role) REFERENCES Role(Id_Role)
);

CREATE TABLE Livre(
   Id_Livre INT AUTO_INCREMENT,
   Titre VARCHAR(50)  NOT NULL,
   Date_Parution DATE NOT NULL,
   Editeur VARCHAR(50)  NOT NULL,
   ISBN VARCHAR(50)  NOT NULL,
   Reserver BOOLEAN NOT NULL,
   Disponible BOOLEAN NOT NULL,
   Date_Retour_Estimer DATE NOT NULL,
   Id_Categorie INT NOT NULL,
   Id_Genre INT NOT NULL,
   ID_Personne INT NOT NULL,
   PRIMARY KEY(Id_Livre),
   UNIQUE(ID_Personne),
   UNIQUE(ISBN),
   FOREIGN KEY(Id_Categorie) REFERENCES Categorie(Id_Categorie),
   FOREIGN KEY(Id_Genre) REFERENCES Genre(Id_Genre),
   FOREIGN KEY(ID_Personne) REFERENCES Personne(ID_Personne)
);

CREATE TABLE emprunter(
   ID_Personne INT,
   Id_Livre INT,
   Date_retour DATE,
   Date_pret DATE,
   PRIMARY KEY(ID_Personne, Id_Livre, Date_retour),
   FOREIGN KEY(ID_Personne) REFERENCES Personne(ID_Personne),
   FOREIGN KEY(Id_Livre) REFERENCES Livre(Id_Livre)
);

CREATE TABLE Ecris(
   Id_Auteur INT,
   Id_Livre INT,
   PRIMARY KEY(Id_Auteur, Id_Livre),
   FOREIGN KEY(Id_Auteur) REFERENCES Auteur(Id_Auteur),
   FOREIGN KEY(Id_Livre) REFERENCES Livre(Id_Livre)
);
