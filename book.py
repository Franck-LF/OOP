# Créer la classe :
#
# Book(title, release_year, author, pages)

from media import Media 


class Book(Media):

    def __init__(self, title:str = '', release_year:int = 0, author:str = '', pages:int = 0):
        super().__init__(title, release_year, 'Book')
        self._author = author
        self._pages = pages

    def display_info(self):
        print('Book')
        print("title", self._title)
        print("release year", self._release_year)
        print("author", self._author)
        print("nb pages", self._pages)

    def __str__(self) -> str:
        return f"Book: {self._title}, {self._release_year}, {self._author}, {self._pages}"

    def to_dict(self):
        dct_temp = super().to_dict()
        dct_temp.update({'type' : 'Book', 'author' : self._author, 'pages' : self._pages})
        return dct_temp

    def from_dict(self, dct):
        assert all([key in ('title', 'release_year', 'author', 'pages') for key in dct.keys()])
        self.__init__(dct['title'], dct['release_year'], dct['author'], dct['pages'])






if __name__ == '__main__':
    book = Book('test', 1980, 'Joe', 120)
    print(book)
    print(book.to_dict())
    book.from_dict({'title' : 'update', 
                     'release_year' : 2000,
                     'author' : 'Jane',
                     'pages' : 3000})
    print(book)