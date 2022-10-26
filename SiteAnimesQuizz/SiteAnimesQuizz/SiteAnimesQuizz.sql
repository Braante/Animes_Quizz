#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: contenu_question
#------------------------------------------------------------

CREATE TABLE contenu_question(
        idContenu      Varchar (50) NOT NULL ,
        libelleContenu Varchar (50) NOT NULL
	,CONSTRAINT contenu_question_PK PRIMARY KEY (idContenu)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: categorie
#------------------------------------------------------------

CREATE TABLE categorie(
        idCategorie  Varchar (50) NOT NULL ,
        libelleCateg Varchar (50) NOT NULL
	,CONSTRAINT categorie_PK PRIMARY KEY (idCategorie)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: anime
#------------------------------------------------------------

CREATE TABLE anime(
        idAnime      Varchar (50) NOT NULL ,
        libelleAnime Varchar (50) NOT NULL ,
        idCategorie  Varchar (50) NOT NULL
	,CONSTRAINT anime_PK PRIMARY KEY (idAnime)

	,CONSTRAINT anime_categorie_FK FOREIGN KEY (idCategorie) REFERENCES categorie(idCategorie)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: questions
#------------------------------------------------------------

CREATE TABLE questions(
        idQuestions     Varchar (50) NOT NULL ,
        libelleQuestion Varchar (50) NOT NULL ,
        idAnime         Varchar (50) NOT NULL
	,CONSTRAINT questions_PK PRIMARY KEY (idQuestions)

	,CONSTRAINT questions_anime_FK FOREIGN KEY (idAnime) REFERENCES anime(idAnime)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: reponse
#------------------------------------------------------------

CREATE TABLE reponse(
        idQuestions Varchar (50) NOT NULL ,
        idContenu   Varchar (50) NOT NULL ,
        correct     Bool NOT NULL
	,CONSTRAINT reponse_PK PRIMARY KEY (idQuestions,idContenu)

	,CONSTRAINT reponse_questions_FK FOREIGN KEY (idQuestions) REFERENCES questions(idQuestions)
	,CONSTRAINT reponse_contenu_question0_FK FOREIGN KEY (idContenu) REFERENCES contenu_question(idContenu)
)ENGINE=InnoDB;

