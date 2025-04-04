# Créer la classe :
#
# Movie(title, release_year, director, duration)

from media import Media 
from typing import List, Dict


class Movie(Media):
    ''' Class object representing a movie '''

    def __init__(self, title:str = '', release_year:int = 0, director:str = '', duration:int = 0):
        ''' Movie constructor.
            
            Args:
             - title (string): title of the album,
             - release_year (int): year of release,
             - director (string): the director's name,
             - duration (int): the movie duration.

            title and release_year are initialized by the parent class (Media).
        '''
        super().__init__(title, release_year, 'Movie')
        self._director = director
        self._duration = duration

    def display_info(self):
        print('Movie')
        print("title", self._title)
        print("release year", self._release_year)
        print("director", self._director)
        print("duration", self._duration)

    def __str__(self) -> str:
        return f"Movie: {self._title}, {self._release_year}, {self._director}, {self._duration}"

    def to_dict(self) -> Dict:
        ''' convert movie into dictionary '''
        dct_temp = super().to_dict()
        dct_temp.update({'type' : 'Movie', 'director' : self._director, 'duration' : self._duration})
        return dct_temp

    def from_dict(self, dct:Dict):
        assert all([key in ('title', 'release_year', 'director', 'duration') for key in dct.keys()])
        self.__init__(dct['title'], dct['release_year'], dct['director'], dct['duration'])





if __name__ == '__main__':
    movie = Movie('test', 1980, 'David Lynch', 90)
    print(movie)
    print(movie.to_dict())
    movie.from_dict({'title' : 'update', 
                     'release_year' : 2000,
                     'director' : 'Steven Spielberg',
                     'duration' : 95})
    print(movie)