# Créer une classe Media (abstraite) avec :
#
# Attributs communs (_title, _release_year)
# Méthode abstraite display_info()
# Méthode to_dict() et from_dict() à redéfinir dans les sous-classes
# Méthode __lt__ pour comparaison par date
# Méthode __str__ pour un affichage lisible


from abc import ABC, abstractmethod
from typing import List, Dict


class Media(ABC):
    ''' Abstract class representing a 'media' object '''

    def __init__(self, title:str, release_year:int, type:str):
        ''' Media constructor.

            Args:
             - the title of the media,
             - the release_year of the media,
             - the type of the media
        '''
        self._title = title
        self._release_year = release_year
        assert type in ['Book', 'Movie', 'Album']
        self._type = type

    def get_title(self) -> str:
        ''' return the title of the media '''
        return self._title

    def get_release_year(self) -> str:
        ''' return the release_year of the media '''
        return self._release_year

    def get_type(self) -> str:
        ''' return the media type '''
        return self._type

    @abstractmethod
    def display_info(self):
        ''' [abstract method] display media informations '''
        pass

    def __str__(self) -> str:
        ''' Return a string with media informations '''
        return f"Media {self.title}, {self._release_year}"

    def __lt__(self, other) -> bool:
        ''' operator to compare 2 medias according to their release_year '''
        return self._release_year < other.release_year
    
    def to_dict(self) -> Dict:
        ''' convert media into dictionary '''
        return {'title' : self._title,
                'release_year' : self._release_year}

    @abstractmethod
    def from_dict(self, dct:Dict):
        pass