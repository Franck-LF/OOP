# Créer la classe :
#
# Movie(title, release_year, director, duration)

from media import Media 


class Movie(Media):

    def __init__(self, title:str, release_year:int, director:str, duration:int):
        super().__init__(title, release_year)
        self._director = director
        self._duration = duration

    def display_info(self):
        pass

    def __str__(self) -> str:
        return f"Movie {self._title}, {self._release_year}, {self._director}, {self._duration}"

    def to_dict(self):
        dct_temp = super().to_dict()
        dct_temp.update({'author' : self._director, 'pages' : self._duration})
        return dct_temp

    def from_dict(self, dct):
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