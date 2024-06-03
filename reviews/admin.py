from django.contrib import admin
from reviews.models import Review

@admin.register(Review)
class ReviewModel(admin.ModelAdmin):
    list_display = ('id', 'filme', 'estrelas', 'comentario')
