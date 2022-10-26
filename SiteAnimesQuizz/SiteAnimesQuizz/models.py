from django.db import models

# test étant la table
class test(models.Model):
    idType = models.IntegerField(primary_key= True) # champ pk
    libelle = models.CharField(max_length = 50)
    class Meta:
        db_table = "test" #nom de la table