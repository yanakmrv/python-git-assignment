import math

def power(a, b):
    return a ** b

def square_root(a):
    return math.sqrt(a)

def factorial(n):
    if n < 0:
        return "Ошибка: факториал отрицательного числа"
    return math.factorial(n)

def percentage(a, b):
    return (a * b) / 100

if __name__ == "__main__":
    print("Продвинутый калькулятор")
    print(f"2^3 = {power(2, 3)}")
    print(f"√16 = {square_root(16)}")
    print(f"5! = {factorial(5)}")
    print(f"20% от 50 = {percentage(50, 20)}")
