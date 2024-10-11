import csv

with open('data.csv', 'r', encoding='utf-8') as file:
    data = file.read()
    students = data.split("; ")
    for student in students:
        name, age, faculty = student.split(", ")
        print(f"Имя: {name}")
        print(f"Возраст: {age}")
        print(f"Факультет: {faculty}\n")


