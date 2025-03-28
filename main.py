# Créer une interface en ligne de commande permettant :
# 
# Se connecter à la base de données MongoDB (en local ou à distance)
# Ajouter un média (en demandant les infos)
# Supprimer un média
# Rechercher un média
# Afficher tous les médias
# Quitter l'application
# 


from library import Library
from media import Media
from book import Book
from movie import Movie
from album import Album
from track import Track

# MongoDB
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



def print_menu(correct_answer_format):
    print('+-------------------------------+')
    print('|  1: Connexion à MongoDB       |')
    print('|  2: Ajouter un média          |')
    print('|  3: Supprimer un média        |')
    print('|  4: Rechercher un média       |')
    print('|  5: Afficher tous les médias  |')
    print("|  6: Quitter l'application     |")
    print('+-------------------------------+')

    if correct_answer_format:
        return input('Saisir une commande\n')
    return input('Saisir une commande entre 1 et 6 !!!\n')


def print_media_type():
    print('-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('0: Quitter')
    print('1: Ajouter un livre')
    print('2: Ajouter un film')
    print('3: Ajouter un album')
    print('-*-*-*-*-*-*-*-*-*-*-*-*-')
    return input('Choisir le type de média\n')


def get_lst_tracks():
    ''' Ask user to write infos about tracks (title + length)
        Return a list of tracks. '''

    lst_tracks = []
    answer_track = None

    while answer_track != 'n':
        answer_track = input('Ajouter une piste (o/n)\n')

        if answer_track == 'o':
            title  = input('Saisir le titre de la piste\n')
            length = int(input('Saisir la durée de la piste\n'))
            lst_tracks.append(Track(title, length))

    return lst_tracks


def get_media(answer_media_type):
    ''' Build a media from user console input '''

    if answer_media_type == 1:
        title = input("Saisir le titre du livre\n")
        year  = int(input("Saisir l'année de publication\n"))
        author = input("Saisir le nom de l'auteur\n")
        pages = int(input("Saisir le nombre de pages\n"))
        return dict(zip(['type', 'title', 'release_year', 'author', 'pages'], ['Book', title, year, author, pages]))

    elif answer_media_type == 2:
        title = input("Saisir le titre du film\n")
        year  = int(input("Saisir l'année de sortie\n"))
        director = input("Saisir le nom du réalisateur\n")
        duration = int(input("Saisir la durée (en minutes)\n"))
        return dict(zip(['type', 'title', 'release_year', 'director', 'duration'], ['Movie', title, year, director, duration]))

    elif answer_media_type == 3:
        title = input("Saisir le titre de l'album\n")
        year  = int(input("Saisir l'année de sortie\n"))
        artist = input("Saisir le nom de l'artiste\n")
        tracks = get_lst_tracks()
        return dict(zip(['type', 'title', 'release_year', 'artist', 'tracks'], ['Album', title, year, artist, tracks]))
        return dict(zip(['type', 'title', 'release_year', 'artist', 'tracks', 'lst_tracks'],
                        ['Album', title, year, artist, tracks, lst_tracks]))


def connect_database():
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = client["multimedia"]
        col_medias = mydb["medias"]
        print("MongoDB connection OK")
        return col_medias
    except ValueError:
        print("Error connecting MongoDB")
    return None


def library_from_mongoDB():
    library = Library()
    library.load_from_mongo()
    return library


answer = None
correct_answer_format = True
col_medias = None

while answer != 6:

    answer = print_menu(correct_answer_format)
    correct_answer_format = answer and answer in '123456'

    if correct_answer_format:
        answer = int(answer)

    if answer == 1:
        # Connect to MongoDB
        col_medias = connect_database()

    elif answer == 2:
        # Add a media
        if col_medias == None:
            print("Connexion à la base de données requise")
        
        else:
            answer_media_type = None

            while answer_media_type != 0:
                answer_media_type = print_media_type()
                correct_answer_type = answer_media_type in '0123'
            
                if correct_answer_type:
                    answer_media_type = int(answer_media_type)
                    
                    if answer_media_type:
                        dct_media = get_media(answer_media_type)
                        col_medias.insert_one(dct_media)
                        answer_media_type = 0

    elif answer == 3:
        # Delete a media
        if col_medias == None:
            print("Connexion à la base de données requise")
        else:
            answer_media_to_delete = input("Nom du média à supprimer\n")
            print(answer_media_to_delete)
            col_medias.delete_one({'title': f'{answer_media_to_delete}'})

    elif answer == 4:
        # Look for a media
        if col_medias == None:
            print("Connexion à la base de données requise")
        else:
            answer_media_to_search = input("Nom du média à rechercher\n")
            library = library_from_mongoDB()
            media = library.search(answer_media_to_search)
            if media:
                print(media)

    elif answer == 5:
        # Display all medias
        if col_medias == None:
            print("Connexion à la base de données requise")
        else:
            library = library_from_mongoDB()
            library.display_all()


print("*** FIN DE L'APPLICATION ***")

