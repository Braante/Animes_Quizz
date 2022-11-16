from django.shortcuts import render
from decimal import Decimal
from unicodedata import decimal
import json
from controller.models import (contenu_question,questions,anime, genre, anime_genre, reponse)

# Create your views here.
def Search(request):
    if request.method == "POST":

        # Données choisies par le client
        post_categorie_anime = request.POST.get("categorie_anime")
        post_nom_anime = request.POST.get("nom_anime")
        post_genre_anime = request.POST.get("genre_anime")

        # Dictionnaire context
        context = {}

        with open("static/json/categ_anime_genre.json") as file:
            json_list_anime_genre = json.load(file)
        
        context["js_json_categ_anime_genre"] = json_list_anime_genre
        
        # Si les données nécessaires sont choisies
        if post_categorie_anime != "" and post_nom_anime != "" and post_genre_anime != "":
            pk_categorie_anime = anime.objects.filter(categorie = post_categorie_anime).values("idAnime")[0]["idAnime"]
            
            pk_nom_anime = anime.objects.filter(libelleAnime = post_nom_anime).values("idAnime")[0]["idAnime"]
            
            pk_genre_anime = genre.objects.filter(libelleGenre = post_genre_anime).values("idGenre")[0]["idGenre"]
        
        # else:
        #     erreur_produit = "Veuillez choisir toutes les informations liées à la sélection de la catégorie."
        #     context["erreur_selection"] = erreur_produit
        #     return render(request, 'controller/accueil.html')
        
        context["categorie_anime"] = post_categorie_anime
        context["nom_anime"] = post_nom_anime
        context["genre_anime"] = post_genre_anime

        return render(request, 'controller/accueil.html')
    
    # Si le post est pas effectué
    else:
        context = {}

        with open("static/json/categ_anime_genre.json") as file:
            json_list_anime_genre = json.load(file)
        
        context["js_json_categ_anime_genre"] = json_list_anime_genre

        return render(request, 'controller/accueil.html')
