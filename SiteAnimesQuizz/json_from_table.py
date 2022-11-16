import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animesquizz.settings')
application = get_wsgi_application()

import json
from controller.models import (contenu_question,questions,anime, genre, anime_genre, reponse)



#remplacer le nom de la fonction par le nom de la table à traiter
def test():
    anime = anime.objects.all().values("idAnime",
        "libelleAnime", "categorie")

    json_list={}
    
    for animes in anime:
        #une variale pour chaque champ
        nom_anime = anime.objects.filter(pk= animes["libelleAnime"]).values("libelleAnime")[0
            ]["libelleAnime"]


        # Format 1er valeur = {}
        if json_list.get(nom_anime) is None:
            json_list[nom_anime] = {} 

        # Format v1 {v2}
        # if json_list[champ].get(champ2) is None:
        #     json_list[champ1][champ2] = {} 

    with open("anime_liste.json", "w", encoding= "utf-8") as file:
        file.write(json.dumps(json_list, indent= 4))

    with open("anime_liste.json", "r") as file:
        datas_rivet = json.load(file)


test()