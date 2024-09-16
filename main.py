"""
1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы
(`make_sound()`, `eat()`) для всех животных.
2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных
и вызывает метод `make_sound()` для каждого животного.
4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
Должны быть методы для добавления животных и сотрудников в зоопарк.
5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
(например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

Дополнительно:
Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл
и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.
"""



import pickle

class Animal:  # базовый класс Animal
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print("Животное ест")


class Bird(Animal):  # подкласс Bird
    def make_sound(self):
        return "Чирик-чирик!"


class Mammal(Animal):  # подкласс Mammal
    def make_sound(self):
        return "Мяу!"


class Reptile(Animal):  # подкласс Reptile
    def make_sound(self):
        return "Шшш!"


def animal_sound(animals):  # функция для демонстрации полиморфизма
    for animal in animals:
        animal.make_sound()


class Zoo:  # класс Zoo для композиции
    def __init__(self):
        self._animals = []
        self._employees = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def get_animals(self):
        return self._animals

    def add_employee(self, employee):
        self._employees.append(employee)

    def get_employees(self):
        return self._employees


    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_file(filename):
        zoo = Zoo()
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
        return zoo


class ZooKeeper(object):  # класс для сотрудников
    def feed_animal(self, animal):
        animal.eat()


class Veterinarian(object):  # ещё один класс для сотрудников
    def heal_animal(self, animal):
        pass


# Пример использования


zoo = Zoo()  # создание зоопарка
bird = Bird("Воробей", 1)  # создание птицы
mammal = Mammal("Кот", 2)  # создание млекопитающего
reptile = Reptile("Змея", 3)  # создание рептилии

zoo.add_animal(bird)  # добавление животных в зоопарк
zoo.add_animal(mammal)
zoo.add_animal(reptile)

animal_sound([bird, mammal, reptile])  # демонстрация

