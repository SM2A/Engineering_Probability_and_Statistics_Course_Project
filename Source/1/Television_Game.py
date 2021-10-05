import numpy
import random
from matplotlib import pyplot

labels = ['10', '100', '1000', '10000']
simulation_values = [10, 100, 1000, 10000]
x = numpy.arange(len(labels))
data = [[0 for a in range(len(simulation_values))] for b in range(3)]

for i in range(len(simulation_values)):

    for _ in range(simulation_values[i]):
        door = [False, False, False]
        prize = random.randint(0, 2)
        door[prize] = True
        selection = [0, 1, 2]
        player_choice = random.choice(selection)
        selection.remove(player_choice)
        instructor_choice = random.choice(selection)
        while door[instructor_choice]:
            instructor_choice = random.choice(selection)
        selection.remove(instructor_choice)
        if door[player_choice]:
            data[0][i] += 1

    for _ in range(simulation_values[i]):
        door = [False, False, False]
        prize = random.randint(0, 2)
        door[prize] = True
        selection = [0, 1, 2]
        player_choice = random.choice(selection)
        selection.remove(player_choice)
        instructor_choice = random.choice(selection)
        while door[instructor_choice]:
            instructor_choice = random.choice(selection)
        selection.remove(instructor_choice)
        player_choice = random.choice(selection)
        if door[player_choice]:
            data[1][i] += 1

    for _ in range(simulation_values[i]):
        door = [False, False, False]
        prize = random.randint(0, 2)
        door[prize] = True
        selection = [0, 1, 2]
        player_choice = random.choice(selection)
        selection.remove(player_choice)
        instructor_choice = random.choice(selection)
        while door[instructor_choice]:
            instructor_choice = random.choice(selection)
        selection.remove(instructor_choice)
        change = int(random.uniform(0, 2))
        if (change % 2) == 1:
            player_choice = random.choice(selection)
        if door[player_choice]:
            data[2][i] += 1

width = 0.6

fig, ax = pyplot.subplots()
rect1 = ax.bar(x - width / 2, data[0], 0.3, label='First Group')
rect2 = ax.bar(x, data[1], 0.3, label='Second Group')
rect3 = ax.bar(x + width / 2, data[2], 0.3, label='Third Group')

ax.set_xlabel('Number of People')
ax.set_ylabel('Number of Winners')
ax.set_title('Number of Winners With Different Group Size')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rect1, padding=3)
ax.bar_label(rect2, padding=3)
ax.bar_label(rect3, padding=3)

fig.tight_layout()

pyplot.show()
