# Работа с файлами
import os

def create_test_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Файл {filename} создан")

def read_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    else:
        return "Файл не существует"

# Пример использования
if __name__ == "__main__":
    create_test_file("test.txt", "Привет, мир!")
    print("Содержимое файла:", read_file("test.txt"))
