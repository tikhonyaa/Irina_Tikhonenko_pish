def addition(num):
    sum = 0;
    x = num
    for i in range(1, len(str(x)) + 1):
        sum += num % 10
        num = int (num / 10)
    print(sum)
n = int(input("Введите число: "))
addition(n)