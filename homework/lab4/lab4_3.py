def intersectList(list1, list2):
    intersection = set(list1) & set(list2)
    sortedInter = sorted(intersection)
    return sortedInter

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = intersectList(list1, list2)
print(result)
