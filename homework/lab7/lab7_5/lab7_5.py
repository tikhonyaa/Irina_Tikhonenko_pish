words = ["level", "world", "radar", "python", "madam"]
palindromes = list(filter(lambda x: x == x[::-1], words))
print(palindromes)
