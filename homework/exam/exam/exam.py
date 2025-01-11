def grainSquare(N):
    return 2 ** (N - 1)

N = int(input())
if 1 <= N <= 64:
    print(grainSquare(N))
else:
    print("ERROR")
