import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Построение случайного блуждания и нанесение точек на диаграмму.
    rw = RandomWalk()
    rw.fill_walk()

    # Назначение размера области просмотра.
    plt.figure(figsize=(10, 6))
    #plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, linewidth=0.1)
    '''
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    #plt.scatter(rw.x_values, rw.y_values, s=1)
    # Выделение первой и последней точек.
    plt.scatter(0, 0, c='green', edgecolors='none', s=5)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=5)
    '''
    # Удаление осей.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break