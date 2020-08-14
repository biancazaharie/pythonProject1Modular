from entities import Melody
from service import Service


def test_entities():
    melody1 = Melody("Furnici","Andries","Folk", 2)
    melody2 = Melody("furnici","Andries","Folk", 2)
    print(melody1 == melody2)


def test_service():
    service = Service()
    print(service.get_all_melodies())
    service.add_melody(Melody("Furnici","Andries","Folk", 2))
    print(service.get_all_melodies())


def test_service2():
    service = Service()
    print(service.get_all_melodies())
    service.add_melody(Melody("Furnici","Colibri","Folk", 2))
    print(service.get_all_melodies())

