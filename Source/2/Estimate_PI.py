import numpy
from matplotlib import pyplot

n = [100, 1000, 10000]
x = [numpy.random.uniform(0, 1, size=n) for n in n]
y = []
var = []

for array in x:
    y_val = []
    for i in array:
        y_val.append(4 * numpy.sqrt(1 - i ** 2))
    y.append(y_val)
    var.append(numpy.var(y_val))
    print(f"var : {numpy.var(y_val)} , avg : {numpy.average(y_val)}")

avg = []

for array in y:
    avg.append(numpy.average(array))

print(avg)

label = ['100', '1000', '10000']
pyplot.errorbar(n, avg, var, linestyle='None', marker='X', elinewidth=1, capsize=6, color='red',label='Estimated PI')
pyplot.xscale('log')
pyplot.xlabel('Number of Samples')
pyplot.ylabel('Value')
pyplot.title('Pi number value with different sample size')
pyplot.grid(which='major', color='b')
pyplot.xticks(n, label)
pyplot.axhline(y=numpy.pi,label='Actual PI')
pyplot.legend()
pyplot.tight_layout()
pyplot.show()
