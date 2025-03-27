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

    def __init__(self, title:str, release_year:int):
        self._title = title
        self._release_year = release_year

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

    def from_dict(self, dct):
        assert all([key in ('title', 'release_year') for key in dct.keys()])
        self = Media(dct['title'], dct['release_year'])





# if __name__ == '__main__':
#     media = Media('test', '1980')