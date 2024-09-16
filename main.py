"""
#[1] Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) [1.1] и методы
(`make_sound()` [1.2], `eat() [1.3]`) для всех животных.
#[2] Реализуйте наследование, создав подклассы `Bird` [2.1], `Mammal` [2.2], и `Reptile` [2.3], которые наследуют
от класса `Animal`. Добавьте специфические атрибуты [2.4 - 2.6] и переопределите методы [2.7 - 2.9], если требуется
(например, различный звук для `make_sound()`).
#[3] Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)` [3.1], которая принимает список
животных [3.2] и вызывает метод `make_sound()` для каждого животного [3.3].
#[4] Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных [4.1],
и сотрудниках [4.2]. Должны быть методы для добавления животных [4.3] и сотрудников [4.4] в зоопарк.
#[5] Создайте классы для сотрудников, например, `ZooKeeper` [5.1], `Veterinarian` [5.2], которые могут иметь
специфические методы (например, `feed_animal()` [5.3] для `ZooKeeper` и `heal_animal()` [5.4] для `Veterinarian`).

Дополнительно:
#[6] Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл
и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.
"""


import json


class Animal:                          # [1]
    def __init__(self, name, age):     # [1.1]
        self.name = name
        self.age = age

    def make_sound(self):              # [1.2]
        print("Generic animal sound")

    def eat(self):                     # [1.3]
        print("Eating...")


class Bird(Animal):                               # [2.1] Класс пчиц
    def __init__(self, name, age, wingspan):            # [2.4] Добавлен атрибут 'wingspan' - размах крыльев
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        print("Чырык-Чырык!")                                   # [2.7] Переопределен метод 'make_sound()'


class Mammal(Animal):                             # [2.2] Класс млекопитающее
    def __init__(self, name, age, fur_color):           # [2.5] Добавлен атрибут 'fur_color' - цвет шерсти
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):                                       # [2.8] Переопределен метод 'make_sound()'
        print("Арррр Аррр Абырвалг!")


class Reptile(Animal):                            # [2.3] Класс рептилоид
    def __init__(self, name, age, scales_color):        # [2.6] Добавлен атрибут 'scales_color' - цвет чешуи
        super().__init__(name, age)
        self.scales_color = scales_color

    def make_sound(self):
        print("Я рептилоид!")                                   # [2.9] Переопределен метод 'make_sound()'


def animal_sound(animals):                   # [3.1] Функция чтобы заставить животне говорить
    for animal in animals:                      # [3.2] Принимает список животных
        if isinstance(animal, Bird):
            animal.make_sound()                     # [3.3] Говори!
        elif isinstance(animal, Mammal):
            animal.make_sound()                     # [3.3] Говори!
        elif isinstance(animal, Reptile):
            animal.make_sound()                     # [3.3] Говори!
        else:
            animal.make_sound()                     # [3.3] Вообще, в принципе говори!


class Zoo:                       # [4] Класс зоопарк
    def __init__(self):
        self.animals = []             # [4.1] Список животных
        self.employees = []           # [4.2] Список сотрудников

    def add_animal(self, animal):           # [4.3] Добавление животного
        self.animals.append(animal)

    def add_employee(self, employee):       # [4.4] Добавление сотрудника
        self.employees.append(employee)

    def display_animals(self):                                                          # ВЫВОД
        for animal in self.animals:                                                     # СПИСКА
            print(f"{animal.name} ({animal.__class__.__name__}) - Age: {animal.age}")   # ЖИВОТНЫХ

    def display_employees(self):                                                         # ВЫВОД
        for employee in self.employees:                                                  # СПИСКА
            print(f"{employee.name} ({employee.__class__.__name__})")                    # СОТРУДНИКОВ

# 98 строка перебор всех из списка self.animals через for с занесением в словарь data
# 99 строка перебор всех из списка self.employees через for с занесением в словарь data
    def save_state(self, filepath):     # [6] Сохранение состояния зоопарка
        with open(filepath, 'w') as f:  # Принимает путь и говорит что можно записывать - 'w'
            data = {'animals': [], 'employees': []}  # Словарь
            data['animals'] = [{'name': a.name, 'age': a.age, 'species': a.__class__.__name__} for a in self.animals]
            data['employees'] = [{'name': e.name, 'type': e.__class__.__name__} for e in self.employees]
            json.dump(data, f, indent=4)  # Сохраняем этот словарь в файл, с отступами 4 пробела

    def load_state(self, filepath):          # Функция загрузки состояния из файла -
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)          # - если он вообще существует
        except FileNotFoundError:
            return

        for d in data['animals']:            # Пробегает по дате
            species = eval(d['species'])     # Преобразует имя в объект класса
            new_attributes = {}
            if 'wingspan' in d:
                new_attributes['wingspan'] = d['wingspan']          # Доп. атрибуты видов
            if 'scales_color' in d:
                new_attributes['scales_color'] = d['scales_color']  # Доп. атрибуты видов
            if 'fur_color' in d:
                new_attributes['fur_color'] = d['fur_color']        # Доп. атрибуты видов
            self.add_animal(species(d['name'], int(d['age']), new_attributes))  # Добавляет животное из словаря 'd'

        for d in data['employees']:         # Пробегает по дате
            type_ = eval(d['type'])         # Преобразует имя в объект класса
            self.add_employee(type_(d['name']))  # Добавляет сотрудника из словаря 'd'


class ZooKeeper:                                     # [5.1] Смотритель
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):                          # [5.3] Кормить
        print(f"{self.name} кормит {animal.name}.")


class Veterinarian:                                  # [5.2] Ветеринар
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):                          # [5.4] Лечить
        print(f"{self.name} лечит {animal.name}.")


if __name__ == "__main__":      # Запускается только если запускается сам MAIN
    import os
    filename = 'zoo_data.json'  # Имя файла с данными (или путь до него)

    # Загружаем данные, если файл существует
    if os.path.exists(filename):
        zoo = Zoo()
        zoo.load_state(filename)
    else:                                                           # Либо делаем дефлотное наполнение зоопарка
        bird = Bird('Воробушык', 10, 'башой')
        mammal = Mammal('ЛевТигор', 7, 'крэмовый с полосками')
        reptile = Reptile('Кукерберг', 5, 'кожанный')


# ТЕСТИРУЕМ

bird = Bird('Омский Пчиц', 10, 'неимоверный размах')
mammal = Mammal('Наш Слоняра', 7, 'базированный цвет')
reptile = Reptile('яшперица', 5, 'непонятный цвет')

zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

keeper = ZooKeeper('Жора')
veterinarian = Veterinarian('Айболит')

zoo.add_employee(keeper)
zoo.add_employee(veterinarian)

print("\nЖивотные:")
zoo.display_animals()
print("\nРаботники:")
zoo.display_employees()

animal_list = [bird, mammal]
animal_sound(animal_list)

keeper.feed_animal(bird)
veterinarian.heal_animal(mammal)

# Сохраняем текущее состояние зоопарка
zoo.save_state(filename)
