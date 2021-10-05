import numpy
import random
from matplotlib import pyplot

n = 2048
result = 0
wins = []

for _ in range(n):

    i = 0
    coin = random.uniform(0, 1)
    while coin > 0.5:
        i += 1
        coin = random.uniform(0, 1)

    if i != 0:
        prize = 2 ** i
        result += prize
        wins.append(prize)
    else:
        wins.append(0)

pyplot.plot(numpy.cumsum(wins),label='Cumulative sum of earnings',color='r')
pyplot.xlabel('Runs')
pyplot.ylabel('Earning ($)')
pyplot.title(f'Earnings in playing game for {n} times')
pyplot.grid()
pyplot.legend()
pyplot.text(650, 480, "Average Earning: "+str(numpy.average(wins)),c='g',fontsize='x-large')
pyplot.show()
print(f"Total winning : {result}")
print(f"Average winning : {numpy.average(wins)}")
