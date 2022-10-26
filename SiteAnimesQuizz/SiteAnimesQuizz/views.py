from django.http import HttpResponse
from django.shortcuts import render

# lien vers le html
def accueil_view(request):
    return HttpResponse('hello')
    # return render(request, 'SitesAnimesQuizz/accueil.html')


