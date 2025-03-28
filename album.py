# Créer la classe :
#
# Album(title, release_year, artist, tracks)
#
# Dans cette classe, ajoutez la possibilité de :
#
# compter le nombre de pistes présentes dans l’album,
# permettre l’utilisation de la fonction len(album) sur une instance de Album,
# afin qu’elle retourne automatiquement le nombre de pistes.


from track import Track
from media import Media 
from typing import List, Dict



class Album(Media):
    ''' Class object representing an album
        contains all informations about album
        and methods to convert it into dictionary
        and update an album from a dictionary.
    '''

    def __init__(self, title:str = '', release_year:int = 0, artist:str = '', tracks:List = []):
        ''' Album Constructor.

            Args:
             - title (string): title of the album,
             - release_year (int): year of release,
             - artist (string): with name of the artist,
             - tracks (list(Track)): list of tracks in the album.

            title and release_year are initialized by the parent class (Media). 
        '''
        super().__init__(title, release_year, 'Album')
        self._artist = artist
        self._tracks = []

        for track in tracks:
            if isinstance(track, Track):
                self._tracks.append(track)
                track.set_album(self)
            elif isinstance(track, dict):
                t = Track(track['title'], track['length'])
                self._tracks.append(t)
                t.set_album(self)


    def display_info(self):
        print('Album')
        print("title", self._title)
        print("release year", self._release_year)
        print("nb tracks", len(self))
        if self._tracks:
            print("lst_tracks", self._lst_tracks)

    def __str__(self) -> str:
        st = f"Album: {self._title}, {self._release_year}, {self._artist}, nb tracks: {len(self)}"
        for track in self._tracks:
            st += f"\n{str(track)}"
        return st

    def __len__(self) -> int:
        return len(self._tracks) if self._tracks else 0

    def to_dict(self) -> Dict:
        ''' convert album into dictionary '''
        dct_temp = super().to_dict()
        lst_dct_tracks = [track.to_dict() for track in self._tracks]
        dct_temp.update({'type' : 'Album', 'artist' : self._artist, 'tracks' : lst_dct_tracks})
        return dct_temp

    def from_dict(self, dct:Dict):
        assert all([key in ('title', 'release_year', 'artist', 'tracks') for key in dct.keys()])
        self.__init__(dct['title'], dct['release_year'], dct['artist'], dct['tracks'])




if __name__ == '__main__':
    album = Album('New Album', 2005, 'Lady Gaga')
    print(album)
    print(album.to_dict())

    track1 = Track('Biz', 195)
    track2 = Track('Jeff', 202)
    track3 = Track('Cece', 188)
    lst_tracks = [track1, track2, track3]

    album.from_dict({'title' : 'update',
                     'release_year' : 2022,
                     'artist' : 'Amy Winehouse',
                     'tracks' : lst_tracks})
    print(album)
    print(album.to_dict())