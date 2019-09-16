import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Чтение дат и температурных максимумов из файла.
filenames1 = 'sitka_weather_2014.csv'
filenames2 = 'death_valley_2014.csv'

with open(filenames1) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates1, highs1, lows1 = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data\n')
        else:
            dates1.append(current_date)
            highs1.append(high)
            lows1.append(low)

    with open(filenames2) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        dates2, highs2, lows2 = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data\n')
            else:
                dates2.append(current_date)
                highs2.append(high)
                lows2.append(low)
    # проверка результата
    print(highs1)
    print(dates1)
    print(lows1)
    print(highs2)
    print(dates2)
    print(lows2)
    # Нанесение данных на диаграмму.
    fig = plt.figure(dpi=64, figsize=(10, 6))
    plt.plot(dates1, highs1, c='red')
    plt.plot(dates2, highs2, c='green')
    # Форматирование диаграммы.
    plt.title("Daily high and low temperatures, July 2014", fontsize=14)
    plt.xlabel('', fontsize=12)
    plt.ylabel("Temperature (F)", fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.show()

"""
    # Нанесение данных на диаграмму.
    fig = plt.figure(dpi=64, figsize=(10, 6))
    plt.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')
    plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)

    # Форматирование диаграммы.
    plt.title("Daily high and low temperatures, July 2014", fontsize=14)
    plt.xlabel('', fontsize=12)

    plt.ylabel("Temperature (F)", fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.show()
"""