s = "aaabbbcccaaadddd"
result = ""
for i in range(len(s)):
    if i == 0 or s[i] != s[i - 1]:
        result += s[i]

print(f"Результат: {result}")

