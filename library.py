# Créer une classe Library contenant une liste de Media
# Avec les méthodes :
#
# add_media(media)
# remove_media(title)
# search(keyword)
# list_medias(order_by='title' ou 'year')
# display_all()
#
# Ajoutez les méthodes suivantes pour MongoDB :
#
# save_to_mongo()
# load_from_mongo()
#

from book import Book
from movie import Movie
from album import Album

# MongoDB
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class Library:

    def __init__(self):
        self._lst_medias = []

    def __len__(self):
        return len(self._lst_medias)

    def __str__(self):
        return '\n'.join([str(media) for media in self._lst_medias])

    def add_media(self, media):
        self._lst_medias.append(media)

    def remove_media(self, title):
        for item in self._lst_medias:
            if item.get_title() == title:
                self._lst_medias.remove(item)

    def search(self, title):
        for item in self._lst_medias:
            if item.get_title() == title:
                return item
        return None

    def list_medias(self, order_by='title'):
        if order_by == 'title':
            self._lst_medias.sort(key = lambda x : x.get_title())
            return self._lst_medias
        elif order_by == 'year':
            self._lst_medias.sort(key = lambda x : x.get_title())
            return self._lst_medias
        else:
            assert False

    def display_all(self):
        for media in self._lst_medias:
            print(media)

    def save_to_mongo(self):
        pass

    def load_from_mongo(self):
        pass



if __name__ == '__main__':
    library = Library()
    print(len(library))
    library.display_all()
    library.add_media(Book('Little Sisters', 1870, 'Jane', 300))
    library.add_media(Movie('Jaws', 1974, 'S. Spielberg', 90))
    library.add_media(Album('Undercover', 2022, 'Papa Roach', 65))
    print(len(library))
    library.display_all()
    print(library.list_medias())
    print(library)
    # library.remove_media('Jaws')
    # print(len(library))
    # library.display_all()
    # print("search:", library.search('Little Sisters'))
