import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Построение случайного блуждания и нанесение точек на диаграмму.
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    #plt.scatter(rw.x_values, rw.y_values, s=1)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break