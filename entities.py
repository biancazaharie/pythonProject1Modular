class Melody:
    """ Clasa Melody avand ca atribute protected title, artist, genre si duration"""

    def __init__(self, title, artist, genre, duration, param_default="default"):
        """ Constructor """
        self._title = title
        self._artist = artist
        self._genre = genre
        self._duration = duration
        # _inseamna ca sunt atribute protected # (nu sunt vizibile dinafara, la fel ca private, in schimb, pot fi mostenite in clase copii)
        # param_default e un parametru optional in constructor, poate fi dat in apelul lui, altfel va lua valoarea default

    def get_title(self):
        """ Getter pentru title """
        return self._title

    def get_artist(self):
        """ Getter pentru artist """
        return self._artist

    def get_genre(self):
        """ Getter pentru genre """
        return self._genre

    def get_duration(self):
        """ Getter pentru duration """
        return self._duration

    def set_title(self, title):
        """ Setter pentru title """
        self._title = title

    def set_artist(self, artist):
        """ Setter pentru artist """
        self._name = artist

    def set_title(self, genre):
        """ Setter pentru genre """
        self._title = genre

    def set_title(self, duration):
        """ Setter pentru duration """
        self._title = duration



    def __repr__(self):
        """ Surprascrierea functiei repr() pentru a converti o melodie la un string cand melodia este continutul unei liste """
        return "Title: {0}, Artist: {1}, Genre: {2}".format(self._title, self._artist, self._genre)

    def __str__(self):
        """ Surprascrierea functiei str() pentru a converti o melodie la un string, sau pentru a o afisa/printa """
        return "Title: {0}, Artist: {1}, Genre: {2}".format(self._title, self._artist, self._genre)


    def __eq__(self, other):
        '''
        Overwrote operator ==
        :param other: a Melody, is given after the operator ==
        :return: True if the Melodies are equal, False otherwise
        '''
        return other.get_title() == self._title and self._artist == other.get_artist()



