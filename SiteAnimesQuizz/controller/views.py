from django.shortcuts import render
from decimal import Decimal
from unicodedata import decimal
from django.shortcuts import render
import json
from controller.models import (contenu_question,questions,anime, genre, anime_genre, reponse)

# Create your views here.
# def test(request):

    # # Données choisies par le client
    # post_libelle = request.POST.get("pet-select")

    # # Dictionnaire context
    # context = {}

    # with open("static/json/products.json") as file:
    #     json_datas_products = json.load(file)
    
    # with open("static/json/colors.json") as file:
    #     json_datas_colors = json.load(file)

    # context["js_json_products"] = json_datas_products

    # animetest = anime.objects.filter(libelleAnime = post_libelle).values("idMatiere")[0]["idMatiere"]

    # context["libelleAnime"] = post_matiere_corps
    
    
    # return render(request, 'rivets/rivet.html', context)

