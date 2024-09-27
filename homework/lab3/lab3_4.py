def maxSum(arr, k):
    if len(arr) < k:
        return None

    resSum = sum(arr[:k])
    maxSum = resSum
    index = 0

    for i in range(1, len(arr) - k + 1):
        resSum = resSum - arr[i - 1] + arr[i + k - 1]
        if resSum > maxSum:
            maxSum = resSum
            index = i
    return maxSum, arr[index:index + k]

arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
k = 3

max, newArr = maxSum(arr, k)
print(newArr)
print(max)

