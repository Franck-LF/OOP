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

from media import Media
from book import Book
from movie import Movie
from album import Album
from typing import List, Dict

# MongoDB
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class Library:

    def __init__(self):
        self._lst_medias:List = []

    def __len__(self) -> int:
        return len(self._lst_medias)

    def __str__(self) -> str:
        return '\n'.join([str(media) for media in self._lst_medias])

    def add_media(self, media:Media):
        self._lst_medias.append(media)

    def remove_media(self, title:str):
        for item in self._lst_medias:
            if item.get_title() == title:
                self._lst_medias.remove(item)

    def search(self, title:str):
        for item in self._lst_medias:
            if item.get_title() == title:
                return item
        return None

    def list_medias(self, order_by:str = 'title'):
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
        if len(self):
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = client["multimedia"]
            col_medias = mydb["medias"]
            col_medias.insert_many([media.to_dict() for media in self._lst_medias])
            print(f"{len(self)} elements added to DB")

    @staticmethod
    def delete_collection_mongoDB():
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = client["multimedia"]
        col_medias = mydb["medias"]
        col_medias.drop()

    @staticmethod
    def __build_object_from_type(type:str) -> Media:
        if type == 'Book':  return Book()
        if type == 'Movie': return Movie()
        if type == 'Album': return Album()
    
    def load_from_mongo(self):
        ''' Load list of medias from MongoDB collection. '''

        client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = client["multimedia"]
        col_medias = mydb["medias"]

        for dct in col_medias.find({}):
            assert 'type' in dct.keys() and '_id' in dct.keys()
            assert dct['type'] in ['Book', 'Movie', 'Album']
            media = Library.__build_object_from_type(dct['type'])
            del dct['_id']
            del dct['type']
            media.from_dict(dct)
            self.add_media(media)




if __name__ == '__main__':
    library = Library()
    # print(len(library))
    # library.display_all()
    # library.add_media(Book('Little Sisters', 1870, 'Jane', 300))
    # library.add_media(Movie('Jaws', 1974, 'S. Spielberg', 90))
    # library.add_media(Album('Undercover', 2022, 'Papa Roach', 65))
    # print(len(library))
    # library.display_all()
    # print(library.list_medias())
    # print(library)
    # library.save_to_mongo()
    library.load_from_mongo()
    # Library.delete_collection_mongoDB()
    # library.remove_media('Jaws')
    print('nb medias:', len(library))
    library.display_all()
    # print("search:", library.search('Little Sisters'))
