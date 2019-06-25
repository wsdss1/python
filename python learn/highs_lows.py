import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Чтение дат и температурных максимумов из файла.
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

    print(highs)
    print(dates)
    # Нанесение данных на диаграмму.
    fig = plt.figure(dpi=64, figsize=(10, 6))
    plt.plot(dates, highs, c='red')
    # Форматирование диаграммы.
    plt.title("Daily high temperatures, July 2014", fontsize=14)
    plt.xlabel('', fontsize=12)
    
    plt.ylabel("Temperature (F)", fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.show()