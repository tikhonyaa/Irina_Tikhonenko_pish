def nod(a, b):
    while b:
        a, b = b, a % b
    return a
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
print(nod(a, b))
