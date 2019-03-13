import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Построение случайного блуждания и нанесение точек на диаграмму.
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=1)
plt.show()

keep_running = input("Make another walk? (y/n): ")
if keep_running == 'n':
    break