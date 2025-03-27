# Créer la classe :
#
# Album(title, release_year, artist, tracks)
#
# Dans cette classe, ajoutez la possibilité de :
#
# compter le nombre de pistes présentes dans l’album,
# permettre l’utilisation de la fonction len(album) sur une instance de Album,
# afin qu’elle retourne automatiquement le nombre de pistes.


import track
from media import Media 
from typing import List, Dict



class Album(Media):

    def __init__(self, title:str = '', release_year:int = 0, artist:str = '', tracks:int = 0, lst_tracks:List = None):
        super().__init__(title, release_year, 'Album')
        self._artist = artist
        self._tracks = tracks
        self._lst_tracks = lst_tracks

    def display_info(self):
        print('Album')
        print("title", self._title)
        print("release year", self._release_year)
        print("nb tracks", self._tracks)
        if self._lst_tracks:
            print("lst_tracks", self._lst_tracks)

    def __str__(self) -> str:
        if self._lst_tracks:
            return f"Album: {self._title}, {self._release_year}, {self._artist}, {self._tracks}, {self._lst_tracks}"
        return f"Album: {self._title}, {self._release_year}, {self._artist}, {self._tracks}"

    def __len__(self) -> int:
        return len(self._lst_tracks) if self._lst_tracks else 0

    def to_dict(self) -> Dict:
        dct_temp = super().to_dict()
        dct_temp.update({'type' : 'Album', 'artist' : self._artist, 'tracks' : self._tracks, 'tracks' : self._lst_tracks})
        return dct_temp

    def from_dict(self, dct):
        assert all([key in ('title', 'release_year', 'artist', 'tracks') for key in dct.keys()])
        self.__init__(dct['title'], dct['release_year'], dct['artist'], dct['tracks'])





if __name__ == '__main__':
    album = Album('New Album', 2005, 'Lady Gaga', 12)
    print(album)
    print(album.to_dict())
    album.from_dict({'title' : 'update',
                     'release_year' : 2022,
                     'artist' : 'Amy Winehouse',
                     'tracks' : 15})
    print(album)