def anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

str1 = "listen"
str2 = "silent"
result = anagrams(str1, str2)

if result:
    print("True")
else:
    print("False")

