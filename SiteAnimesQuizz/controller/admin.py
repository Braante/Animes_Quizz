from django.contrib import admin

# Register your models here.
from controller.models import (contenu_question,questions,anime, genre, anime_genre, reponse)

admin.site.register(contenu_question)
admin.site.register(questions)
admin.site.register(anime)
admin.site.register(genre)
admin.site.register(anime_genre)
admin.site.register(reponse)
