def unique(sentence):
    words = sentence.split()
    uniqueW = set(words)
    sortedW = sorted(uniqueW)
    return sortedW

sentence = "apple banana apple orange banana kiwi"
result = unique(sentence)
print(result)

