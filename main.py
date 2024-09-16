def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Пример использования
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print(f"Наибольший общий делитель {num1} и {num2} = {gcd(num1, num2)}")
