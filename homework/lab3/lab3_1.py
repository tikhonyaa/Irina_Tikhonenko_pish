def cycSh(arr, shift):
    shift = shift % len(arr)
    return arr[-shift:] + arr[:-shift]

arr = [1, 2, 3, 4, 5]
shift = 2
shiftArr = cycSh(arr, shift)
print(shiftArr)

