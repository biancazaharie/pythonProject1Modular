from entities import Melody
from service import Service


class ConsoleUI:
    def __init__(self, service: Service):
        """
        The constructor of the ConsoleUI class
        :param service: the service of the app (Service)
        """
        self.__service = service

    def __validate_duration(self, duration):
        try:
            duration = float(duration)
        except Exception:
            raise ValueError("Duration of the melody must be a float")

    def __add_melody(self):
        title = input("Enter the title of the melody: ")
        artist = input("Enter the artist of the melody: ")
        genre = input("Enter the genre of the melody: ")
        duration = input("Enter the duration of the melody: ")

        self.__validate_duration(duration)
        self.__service.add_melody(Melody(title, artist, genre, float(duration)))

    def __update_melody(self):
        old_title = input("Enter the old title of the melody: ")
        title = input("Enter the new title of the melody: ")
        artist = input("Enter the new artist of the melody: ")
        genre = input("Enter the new genre of the melody: ")
        duration = input("Enter the new duration of the melody: ")

        self.__validate_duration(duration)
        self.__service.update_melody(old_title, Melody(title, artist, genre, float(duration)))


    def __delete_melody(self):
        title = input("Title of the melody you want to delete: ")
        self.__service.delete_melody(title)

    def __print_average_duration(self):
        duration = self.__service.average_duration()
        print("The average duration of all the melodies is {0}".format(duration))

    def __print_most_popular_genre(self):
        get_max_genre = self.__service.most_popular_genre()
        print("The most popular genre of all the melodies is {0}".format(get_max_genre))


    def __print_all_melodies(self):
        melodies = self.__service.get_all_melodies()
        for melody in melodies:
            print(melody)

    def __print_menu(self):
        print("1. Add melody")
        print("2. Delete melody")
        print("3. Average duration of all melodies")
        print("4. Print melodies")
        print("5. Print most popular genre")
        print("6. Update melody")
        print("0. Exit")

    def run(self):
        options = {
            '1': self.__add_melody,
            '2': self.__delete_melody,
            '3': self.__print_average_duration,
            '4': self.__print_all_melodies,
            '5': self.__print_most_popular_genre,
            '6': self.__update_melody
        }
        while True:
            self.__print_menu()
            command = input("\nEnter the command: ").strip()
            try:
                if command == '0':
                    break
                options[command]()
            except Exception as ex:
                print(ex)
