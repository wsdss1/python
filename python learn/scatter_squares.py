import matplotlib.pyplot as plt


x_values = list(range(1, 500))
y_values = [x**3 for x in x_values]
#c=(0, 0, 0.8)  / c='green' /c=y_values, cmap=plt.cm.Blues,
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=1)
# Назначение заголовка диаграммы и меток осей.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', which='major', labelsize=15)
# Назначение диапазона для каждой оси.
plt.axis([0, 500, 0, 125000000])

plt.show()