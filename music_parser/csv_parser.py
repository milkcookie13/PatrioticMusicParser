from .models import Song
import csv 

def load_csv_data(path=None):
    if not path:
        path = './data.csv'
        
    with open(path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                
                song = Song(
                    name=row['Название'],
                    composer=row.get('Композитор', ''),
                    musical_genre=row.get('Музыкальный жанр', ''),
                    theme=row.get('Тема', ''),
                    year_of_creation=row.get('Год создания', '')
                )
                song.save()
