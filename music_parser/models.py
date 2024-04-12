from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название песни')
    composer = models.CharField(max_length=255, verbose_name='Исполнитель')
    musical_genre = models.CharField(max_length=255, verbose_name='Музыкальный жанр')
    theme = models.CharField(max_length=255, blank=True, verbose_name='Смысл песни')
    year_of_creation = models.CharField(max_length=32, blank=True)

