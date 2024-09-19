def f(x):
    if -2 <= x < 2:
        return x ** 2
    elif x >= 2:
        return x ** 2 + 4 * x + 5
    elif x < -2:
        return 4
num = int(input("Введите число: "))
print(f(num))
