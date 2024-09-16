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


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Generic animal sound")

    def eat(self):
        print("Eating...")


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        print("Tweet tweet!")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print("Roar!")


class Reptile(Animal):
    def __init__(self, name, age, scales_color):
        super().__init__(name, age)
        self.scales_color = scales_color

    def make_sound(self):
        print("Hisssss!")


def animal_sound(animals):
    for animal in animals:
        if isinstance(animal, Bird):
            animal.make_sound()
        elif isinstance(animal, Mammal):
            animal.make_sound()
        elif isinstance(animal, Reptile):
            animal.make_sound()
        else:
            animal.make_sound()


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_animals(self):
        for animal in self.animals:
            print(f"{animal.name} ({animal.__class__.__name__}) - Age: {animal.age}")

    def display_employees(self):
        for employee in self.employees:
            print(f"{employee.name} ({employee.__class__.__name__})")


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} feeds {animal.name}.")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} heals {animal.name}.")


# Пример использования
bird = Bird('Tweety', 10, 'small')
mammal = Mammal('Lion', 7, 'golden')
reptile = Reptile('Snake', 5, 'green')

zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

keeper = ZooKeeper('Joe')
veterinarian = Veterinarian('Dr. Alex')

zoo.add_employee(keeper)
zoo.add_employee(veterinarian)

print("\nAnimals in the zoo:")
zoo.display_animals()
print("\nEmployees in the zoo:")
zoo.display_employees()

animal_list = [bird, mammal]
animal_sound(animal_list)

keeper.feed_animal(bird)
veterinarian.heal_animal(mammal)