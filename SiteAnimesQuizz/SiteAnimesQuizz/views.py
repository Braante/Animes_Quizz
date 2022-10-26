from django.shortcuts import render

# lien vers le html
def accueil_view(request):
    return render(request, 'rivecol/accueil.html')

def contact_view(request):
    return render(request, 'rivecol/contact.html')