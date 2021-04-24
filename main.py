import Methods
from math import exp, sin
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

# Исследуемая функция
f = lambda x: exp(sin(x)) * (x ** 2)

# Начальные значения
a = -5.1        # левая граница            
b = 2.4         # правая граница
eps = 1e-5

methods = {'Dichotomy': Methods.Dichotomy,
           'Golden_ratio': Methods.Golden_ratio,
           'Fibonacci': Methods.Fibonacci,
           'Parabolas': Methods.Parabolas,
           'Brent': Methods.Brent}

for key, method in methods.items():
    iterations = []
    # f_calculations = []

    for i in range(15):
        eps = 1 / 10 ** i               # точность
        iterations.append(method(f, a, b, eps)[1])
        # f_calculations.append(method(f, a, b, eps)[2]) 

    x = np.arange(1, 16)
    y = iterations
    # y = f_calculations

    xnew = np.linspace(x.min(), x.max(), 100) 
    bspline = interpolate.make_interp_spline(x, y)
    y_smoothed = bspline(xnew)
    plt.plot(xnew, y_smoothed, label = key)

plt.title("Сравнение методов по кол-ву итераций")
# plt.title("Сравнение методов по кол-ву вызовов ф-ии")
plt.xlabel('Точность')
plt.ylabel('Кол-во итераций')
# plt.ylabel('Кол-во вызовов ф-ии')
plt.legend(loc = 'best')
plt.show()
