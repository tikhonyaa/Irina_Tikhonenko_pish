import re

text = "Контакты: ivanov@example.com, petrov@work.net, sid@mail.ru"
emails = re.findall(r'\b[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(emails)

