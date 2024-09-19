def addMulti(num):
    sum = 0;
    multi = 1;
    x = num
    for i in range(1, len(str(x)) + 1):
        sum += num % 10
        multi *= num % 10
        num = int (num / 10)
    print(sum == multi)
n = int(input("Введите число для проверки: "))
addMulti(n)