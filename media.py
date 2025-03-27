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

    def __init__(self, title:str, release_year:int, type:str):
        self._title = title
        self._release_year = release_year
        assert type in ['Book', 'Movie', 'Album']
        self._type = type

    def get_title(self):
        ''' accessor '''
        return self._title

    def get_release_year(self):
        ''' accessor '''
        return self._release_year

    def get_type(self):
        return self._type

    @abstractmethod
    def display_info(self):
        pass

    def __str__(self) -> str:
        return f"Media {self.title}, {self._release_year}"

    def __lt__(self, other) -> bool:
        return self._release_year < other.release_year
    
    def to_dict(self):
        return {'title' : self._title,
                'release_year' : self._release_year}

    @abstractmethod
    def from_dict(self, dct):
        pass