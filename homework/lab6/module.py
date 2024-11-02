def f(x):
    if -2 <= x < 2:
        return x ** 2
    elif x >= 2:
        return x ** 2 + 4 * x + 5
    elif x < -2:
        return 4

def nod(a, b):
    while b:
        a, b = b, a % b
    return a

def add_multi(num):
    total_sum = 0
    total_multi = 1
    x = num
    while x > 0:
        digit = x % 10
        total_sum += digit
        total_multi *= digit
        x //= 10
    return total_sum == total_multi

def addition(num):
    total_sum = 0
    x = num
    while x > 0:
        total_sum += x % 10
        x //= 10
    return total_sum