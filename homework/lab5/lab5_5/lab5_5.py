import re

text = "Сегодня 20 градусов, завтра будет 18 градусов, а вчера было 22 градуса."
numbers = re.findall(r'\d+', text)
numbers = list(map(int, numbers))

print(numbers)

