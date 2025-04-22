# OOP-zoo

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Z01coder/OOP-zoo/blob/main/LICENSE)

## Описание проекта

Этот проект представляет собой учебный пример работы с объектно-ориентированным программированием (ООП) на Python. В нем реализованы базовые принципы ООП, такие как инкапсуляция, наследование и полиморфизм. Проект демонстрирует создание классов, управление атрибутами и методами, а также взаимодействие между объектами.

Основной код программы находится в файле [`main.py`](https://github.com/Z01coder/OOP-zoo/blob/main/main.py).

---

## Структура проекта

### Классы:

1. **Класс `User`**: <br>
   - **Описание**: Представляет обычного пользователя системы. <br>
   - **Атрибуты**: <br>
     - `_id`: Уникальный идентификатор пользователя. <br>
     - `_name`: Имя пользователя. <br>
     - `_access_level`: Уровень доступа (`'user'` по умолчанию). <br>
   - **Методы**: <br>
     - Геттеры и сеттеры для доступа к атрибутам (`id`, `name`, `access_level`). <br>

2. **Класс `Admin`** (наследуется от `User`): <br>
   - **Описание**: Представляет администратора системы с расширенными правами. <br>
   - **Дополнительные атрибуты**: <br>
     - `_access_level`: Уровень доступа администратора (`'admin'`). <br>
   - **Методы**: <br>
     - `add_user(new_user)`: Добавляет нового пользователя в систему. <br>
     - `remove_user(user_to_remove)`: Удаляет пользователя из системы. <br>

---

## Установка и использование

1. **Клонирование репозитория**:
   ```bash
   git clone https://github.com/Z01coder/OOP-zoo.git
   cd OOP-zoo

2. **Запуск проекта**:
   ```bash
   python main.py

3. **Пример кода**:
```bash
from main import User, Admin

# Создание обычного пользователя
user1 = User(id=1, name="John Doe")
print(f"User ID: {user1.id}, Name: {user1.name}, Access Level: {user1.access_level}")

# Создание администратора
admin = Admin(id=2, name="Jane Admin", access_level="admin")
print(f"Admin ID: {admin.id}, Name: {admin.name}, Access Level: {admin.access_level}")

# Добавление пользователя через администратора
admin.add_user(user1)
