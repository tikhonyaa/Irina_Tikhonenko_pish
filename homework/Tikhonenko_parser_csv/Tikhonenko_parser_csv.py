import argparse
import csv
from collections import defaultdict
import statistics
import sys

# чтение и проверка формата csv файла
def readCsv(filePath):
    data = []
    try:
        with open(filePath, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for lineNum, row in enumerate(reader, start=1):
                if len(row) != 6:
                    print(f"Ошибка форматирования в строке {lineNum}: {row}")
                    continue
                data.append(row)
        return data
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

# фильтрация и преобразование данных
def processData(data):
    monthlyData = defaultdict(list)
    yearlyTemp = []

    for row in data:
        year, month, day, hour, minute, temp = row

        try:
            temp = int(temp)
        except ValueError:
            print(f"Ошибка: некорректная температура в строке: {row}")
            continue

        monthlyData[month].append(temp)
        yearlyTemp.append(temp)

    return monthlyData, yearlyTemp

# вычисление статистики
def statistic(monthlyData, yearlyTemp):
    stats = {}

    for month, temps in monthlyData.items():
        if temps:
            stats[month] = {
                'avg': round(statistics.mean(temps), 2),
                'min': min(temps),
                'max': max(temps)
            }

    if yearlyTemp:
        yearlyStats = {
            'avg': round(statistics.mean(yearlyTemp), 2),
            'min': min(yearlyTemp),
            'max': max(yearlyTemp)
        }
    else:
        yearlyStats = {}

    return stats, yearlyStats

# вывод статистики
def printStat(stats, yearlyStats, month=None):
    if month:
        month = f"{int(month):02d}"
        if month in stats:
            print(f"Статистика за {month} месяц:")
            print(f"Средняя температура: {stats[month]['avg']}°C")
            print(f"Минимальная температура: {stats[month]['min']}°C")
            print(f"Максимальная температура: {stats[month]['max']}°C")
        else:
            print(f"Нет данных для месяца {month}.")
    else:
        print("Статистика по месяцам:")
        for month, data in sorted(stats.items()):
            print(f"Месяц {month}: Средняя: {data['avg']}°C, Минимум: {data['min']}°C, Максимум: {data['max']}°C")

        print("\nСтатистика за год:")
        print(f"Среднегодовая температура: {yearlyStats['avg']}°C")
        print(f"Минимальная температура за год: {yearlyStats['min']}°C")
        print(f"Максимальная температура за год: {yearlyStats['max']}°C")

def main():
    parser = argparse.ArgumentParser(description='Программа для анализа температурных данных за год')
    parser.add_argument('-f', '--file', type=str, help='CSV-файл с температурными данными', required=True)
    parser.add_argument('-m', '--month', type=int, help='Номер месяца для вывода статистики', required=False)

    # Проверка на отсутствие аргументов
    if len(sys.argv) == 1:
        parser.print_help()
        print("help")
        sys.exit()

    args = parser.parse_args()

    # чтение данных из csv
    csvData = readCsv(args.file)
    if csvData is None:
        return

    # обработка данных
    monthlyData, yearlyTemp = processData(csvData)
    
    # подсчет статистики
    monthlyStats, yearlyStats = statistic(monthlyData, yearlyTemp)

    # вывод статистики
    printStat(monthlyStats, yearlyStats, args.month)

if __name__ == '__main__':
    main()
