from entities import Melody


class Service:
    def __init__(self):
        self.__melodies = []
        # read from file / DB
        # self.read_from_file()
        self.__melodies.append(Melody("Vremuri", "Pasarea colibri", "Folk", 3.25))
        self.__melodies.append(Melody("Wind of change", "Scorpions", "Rock", 4.3))
        self.__melodies.append(Melody("Ti-am dat un inel", "Dan Bitman", "Pop", 2.4))

    def get_all_melodies(self):
        """
        Returns the list of all melodies.
        :return: the list of all melodies (list)
        """
        return self.__melodies

    def add_melody(self, new_melody):
        """
        Adds a given melody to the melody list.
        If the melody already exists, raise ValueError
        :param melody: param to add to the list of melodies (Melody)
        """
        for melody in self.__melodies:
            if melody == new_melody:
                raise ValueError("The melody already exists!")
        self.__melodies.append(new_melody)


    def average_duration(self):
        """
        Returns the average duration of all the melodies in the list
        :return: average duration of all the melodies in the list
        """
        sum = 0
        for melody in self.__melodies:
            sum += melody.get_duration()
        return sum / len(self.__melodies)

    def most_popular_genre(self):
        """
         Returns the most popular genre of all the melodies in the list
         :return: most popular genre of all the melodies in the list
         """

        my_dictionary = {"Folk": 0, "Rock": 0, "Pop": 0}
        # key => value
        i = 1
        for melody in self.__melodies:
            if melody.get_genre() in my_dictionary:
                my_dictionary[melody.get_genre()] = my_dictionary[melody.get_genre()] + 1
            elif not (melody.get_genre() in my_dictionary):
                my_dictionary.update({melody.get_genre(): i})
        max = 0
        get_max_genre = ""

        for x in my_dictionary.keys():
            if my_dictionary[x] > max:
                max = my_dictionary[x]
                get_max_genre = x
        return get_max_genre


    def delete_melody(self, title):
        """
        Deletes a melody with a given title
        :param title: title of the melody to be deleted
        :return: Nothing
        """
        position = self.__find_position_of_melody(title)
        if position == -1:
            raise ValueError("The melody named {0} doesn't exist!".format(title))
        else:
            del self.__melodies[position]

    def __find_position_of_melody(self, title):
        """
        Finds the position of a melody, given by the title, in the melody list
        :param name: the given title (str)
        :return: the position of the given melody or -1 (int)
        """
        for i in range(len(self.__melodies)):
            if self.__melodies[i].get_title() == title:
                return i
        return -1

    def update_melody(self, old_title, new_melody):
        """
        Updates a given melody with new information.
        If the melody doesn't exists, raise ValueError
        :param melody: param to add to the  list of melodies (Melody)
        """
        i = self.__find_position_of_melody(old_title)
        if i > -1:
            self.__melodies[i] = new_melody

#modificare de test