def cyclicShift(arr, shift):
    shift = shift % len(arr)
    return arr[-shift:] + arr[:-shift]

def shiftMatrix(matrix, shift):
    return [cyclicShift(sublist, shift) for sublist in matrix]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
shift = 1

shiftedMatrix = shiftMatrix(matrix, shift)
for sublist in shiftedMatrix:
    print(sublist)

