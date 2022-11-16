import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animesquizz.settings')
application = get_wsgi_application()

import json
from controller.models import (contenu_question,questions,anime, genre, anime_genre, reponse)



#remplacer le nom de la fonction par le nom de la table à traiter
def QuizzanimeJSON():
    animesGenre = anime_genre.objects.all().values("idAnime",
        "idGenre").order_by( "idAnime","idGenre")

    json_list_anime_genre={}
    
    for animeGenre in animesGenre:
        #une variale pour chaque champ
        categorie_anime = anime.objects.filter(pk= animeGenre["idAnime"]).values("categorie")[0
                    ]["categorie"]

        nom_anime = anime.objects.filter(pk= animeGenre["idAnime"]).values("libelleAnime")[0
            ]["libelleAnime"]

        genre_anime = genre.objects.filter(pk= animeGenre["idGenre"]).values("libelleGenre")[0
            ]["libelleGenre"]


        # Liste des catégories
        if json_list_anime_genre.get(categorie_anime) is None:
            json_list_anime_genre[categorie_anime] = {} 

        # Liste des animes dependant de la catégorie
        if json_list_anime_genre[categorie_anime].get(nom_anime) is None:
            json_list_anime_genre[categorie_anime][nom_anime] = []
        
        # Liste des genres dépendant des listes précédantes
        json_list_anime_genre[categorie_anime][nom_anime].append(genre_anime)

    with open("categ_anime_genre.json", "w", encoding= "utf-8") as file:
        file.write(json.dumps(json_list_anime_genre, indent= 4))

    with open("categ_anime_genre.json", "r") as file:
        datas_anime = json.load(file)


QuizzanimeJSON()