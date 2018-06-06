# =========================================================
# =============     LINEAL REGRESSION    ==================
# =========================================================
from matplotlib import pyplot
from numpy import linspace
from math import sqrt
import json

Data = json.load(open('LinearRegression.json'))

y = Data['VerticalAxis']
x = Data['HorizontalAxis']
n = len(x)

SumOfSumOfXiSumOfYi, SumOfXi, SumOfYi, SumOfXi2, SumOfYi2 = 0, 0, 0, 0, 0

for i in range(n):
    SumOfSumOfXiSumOfYi += x[i] * y[i]
    SumOfXi   += x[i]
    SumOfYi   += y[i]
    SumOfXi2  += x[i] * x[i]
    SumOfYi2  += y[i] * y[i]


m = (n * SumOfSumOfXiSumOfYi - SumOfXi * SumOfYi) / (n * SumOfXi2 - SumOfXi * SumOfXi)
b = (SumOfXi2 * SumOfYi - SumOfXi * SumOfSumOfXiSumOfYi) / (n * SumOfXi2 - SumOfXi * SumOfXi)
p = (SumOfSumOfXiSumOfYi - SumOfXi * SumOfYi / n)                                               \
    /sqrt((SumOfXi2 - SumOfXi * SumOfXi / n) * (SumOfYi2 - SumOfYi * SumOfYi / n))

Result = f"Line: y = {round(m, 4)}x + {round(b, 4)}. Pearson: {round(p, 4)}"

space = linspace(100, 150, 1000)
pyplot.plot(x, y, 'o')
pyplot.plot(space, m * space + b)
pyplot.suptitle(Result)
pyplot.show()
