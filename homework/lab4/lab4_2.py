def charFreq(sentence):
    frequency = {}
    for char in sentence:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

sentence = "abracadabra"
result = charFreq(sentence)

for char, freq in result.items():
    print(f"'{char}': {freq}")

