#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: anime
#------------------------------------------------------------

CREATE TABLE anime(
        idAnime      Varchar (50) NOT NULL ,
        libelleAnime Varchar (50) NOT NULL ,
        categorie    Varchar (50) NOT NULL
	,CONSTRAINT anime_PK PRIMARY KEY (idAnime)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: questions
#------------------------------------------------------------

CREATE TABLE questions(
        idQuestion      Varchar (50) NOT NULL ,
        libelleQuestion Varchar (50) NOT NULL ,
        idAnime         Varchar (50) NOT NULL
	,CONSTRAINT questions_PK PRIMARY KEY (idQuestion)

	,CONSTRAINT questions_anime_FK FOREIGN KEY (idAnime) REFERENCES anime(idAnime)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: contenu_question
#------------------------------------------------------------

CREATE TABLE contenu_question(
        idContenu      Varchar (50) NOT NULL ,
        libelleContenu Varchar (50) NOT NULL
	,CONSTRAINT contenu_question_PK PRIMARY KEY (idContenu)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: genre
#------------------------------------------------------------

CREATE TABLE genre(
        idGenre      Varchar (50) NOT NULL ,
        libelleGenre Varchar (50) NOT NULL
	,CONSTRAINT genre_PK PRIMARY KEY (idGenre)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: reponse
#------------------------------------------------------------

CREATE TABLE reponse(
        idQuestion Varchar (50) NOT NULL ,
        idContenu  Varchar (50) NOT NULL ,
        correct    Bool NOT NULL
	,CONSTRAINT reponse_PK PRIMARY KEY (idQuestion,idContenu)

	,CONSTRAINT reponse_questions_FK FOREIGN KEY (idQuestion) REFERENCES questions(idQuestion)
	,CONSTRAINT reponse_contenu_question0_FK FOREIGN KEY (idContenu) REFERENCES contenu_question(idContenu)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: anime_genre
#------------------------------------------------------------

CREATE TABLE anime_genre(
        idAnime Varchar (50) NOT NULL ,
        idGenre Varchar (50) NOT NULL
	,CONSTRAINT anime_genre_PK PRIMARY KEY (idAnime,idGenre)

	,CONSTRAINT anime_genre_anime_FK FOREIGN KEY (idAnime) REFERENCES anime(idAnime)
	,CONSTRAINT anime_genre_genre0_FK FOREIGN KEY (idGenre) REFERENCES genre(idGenre)
)ENGINE=InnoDB;

