from django.db import models

# test étant la table
class contenu_question(models.Model):
    idContenu = models.IntegerField(primary_key= True) # champ pk
    libelleContenu = models.CharField(max_length = 50)
    class Meta:
        db_table = "contenu_question" #nom de la table

class questions(models.Model):
    idQuestion = models.IntegerField(primary_key= True) # champ pk
    libelleQuestion = models.CharField(max_length = 50)
    idAnime = models.IntegerField()
    class Meta:
        db_table = "questions" #nom de la table

class anime(models.Model):
    idAnime = models.IntegerField(primary_key= True) # champ pk
    libelleAnime = models.CharField(max_length = 50)
    categorie = models.CharField(max_length = 50)
    class Meta:
        db_table = "anime" #nom de la table


class genre(models.Model):
    idGenre = models.IntegerField(primary_key= True) # champ pk
    libelleGenre = models.CharField(max_length = 50)
    class Meta:
        db_table = "genre" #nom de la table

class anime_genre(models.Model):
    idGenre = models.IntegerField(primary_key= True) # champ pk
    idAnime = models.IntegerField()
    class Meta:
        db_table = "anime_genre" #nom de la table

class reponse(models.Model):
    idQuestion = models.IntegerField(primary_key= True) # champ pk
    idContenu = models.IntegerField()
    correct = models.BooleanField()
    class Meta:
        db_table = "reponse" #nom de la table