# Créez une classe Track(title, length (seconds)) 
# pour représenter une piste d’un album. 
# Cette classe devra elle aussi inclure une méthode to_dict().


class Track:
    ''' Class object representing a track '''

    def __init__(self, title:str = '', length:int = 0):
        ''' track Constructor 

            Args:
             - title (string): title of the track,
             - length (int): duration of the track (in minutes),
        '''
        self._title = title
        self._length = length

    def display_info(self):
        print('Track')
        print("title", self._title)
        print("length", self._length)

    def __str__(self) -> str:
        return f"Track: {self._title}, {self._length}"

    def to_dict(self):
        return {'title' : self._title, 'length' : self._length}

    def from_dict(self, dct):
        assert all([key in ('title', 'length') for key in dct.keys()])
        self.__init__(dct['title'], dct['length'])



if __name__ == '__main__':
    track = Track('New hate', 200)
    print(track)
    print(track.to_dict())
