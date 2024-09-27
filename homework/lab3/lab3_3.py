def reverseBlock(arr, block_size):
    result = []

    for i in range(0, len(arr), blockSize):
        block = arr[i:i + blockSize]
        if len(block) == blockSize:
            result.extend(block[::-1]) 
        else:
            result.extend(block) 

    return result

arr = [1, 2, 3, 4, 5, 6, 7]
blockSize = 3
reversedBlock = reverseBlock(arr, blockSize)
print(reversedBlock)

