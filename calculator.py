# Простой калькулятор
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка: деление на ноль"

if __name__ == "__main__":
    print("Калькулятор")
    print("2 + 3 =", add(2, 3))
    print("5 - 1 =", subtract(5, 1))
