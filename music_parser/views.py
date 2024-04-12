import csv
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Song
from django.shortcuts import render
from .serializers import SongSerializer
from .csv_parser import load_csv_data
from django.db.models import Q

def index(request):  #  Главная страница
    return render(request, 'index.html')


def load_data_view(request):
    Song.objects.all().delete() #  Очистка базы данных перед скачиванием файлов
    load_csv_data()
    return HttpResponse("Data loaded successfully!")

    
class MusicAPIView(APIView):
    def get(self, request):
        # Получаем параметры для поиска
        name = request.GET.get('name')
        composer = request.GET.get('composer')
        musical_genre = request.GET.get('genre')
        year_of_creation = request.GET.get('year')
        theme = request.GET.get('theme')

        # Формируем фильтр на основе переданных параметров поиска
        filters = Q()
        if name:
            filters &= Q(name__icontains=name)
        if composer:
            filters &= Q(composer__icontains=composer)
        if musical_genre:
            filters &= Q(musical_genre__icontains=musical_genre)
        if year_of_creation:
            filters &= Q(year_of_creation__icontains=year_of_creation)
        if theme:
            filters &= Q(theme__icontains=theme)

        # Применяем фильтр к запросу песен
        songs = Song.objects.filter(filters)
        serializer = SongSerializer(songs, many=True)
        return Response({'songs': serializer.data})
