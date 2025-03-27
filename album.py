# Créer la classe :
#
# Album(title, release_year, artist, tracks)

from media import Media 


class Album(Media):

    def __init__(self, title:str, release_year:int, artist:str, tracks:int):
        super().__init__(title, release_year)
        self._artist = artist
        self._tracks = tracks

    def display_info(self):
        pass

    def __str__(self) -> str:
        return f"Album {self._title}, {self._release_year}, {self._artist}, {self._tracks}"

    def to_dict(self):
        dct_temp = super().to_dict()
        dct_temp.update({'artist' : self._artist, 'tracks' : self._tracks})
        return dct_temp

    def from_dict(self, dct):
        assert all([key in ('title', 'release_year', 'artist', 'tracks') for key in dct.keys()])
        self.__init__(dct['title'], dct['release_year'], dct['artist'], dct['tracks'])





if __name__ == '__main__':
    album = Album('New Album', 2005, 'Lady Gaga', 12)
    print(album)
    print(album.to_dict())
    album.from_dict({'title' : 'update', 
                     'release_year' : 2022
                     'artist' : 'Amy Winehouse',
                     'tracks' : 15})
    print(album)