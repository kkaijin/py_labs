import argparse

# Создаем парсер
parser = argparse.ArgumentParser(description="Пример скрипта с argparse")

# Добавляем аргументы
parser.add_argument("-n", "--name", help="Ваше имя", required=True)
parser.add_argument("-a", "--age", help="Ваш возраст", type=int)

# Парсим аргументы
args = parser.parse_args()

# Используем аргументы
print(f"Привет, {args.name}! Тебе {args.age} лет.")