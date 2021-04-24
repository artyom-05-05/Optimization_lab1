
import random
from math import sqrt

# Метод дихотомии
def Dichotomy(f, a, b, eps): 
    delta = eps/2               # величина отступа
    
    iterations = 0              # кол-во итераций алгоритма
    f_calculations = 0          # кол-во вычислений ф-ии

    while (b - a >= eps):

        x_mean = (a + b) / 2    # Находим координату середины отрезка
        F1 = f(x_mean - delta)  # Вычисляем значения ф-ии в окрестности данной точки
        F2 = f(x_mean + delta)

        if (F1 < F2):           # Сравниваем F1 и F2 и отбрасываем одну из половин отрезка [a, b]
            b = x_mean
        else:
            a = x_mean

        iterations += 1         # Увеличиваем счётчики
        f_calculations += 2

        # print(f"{iterations} итерация: отрезок [{a}, {b}]")

    return (a+b)/2, iterations, f_calculations

# ----------------------------------------------------------------------

# Метод золотого сечения
def Golden_ratio(f, a, b, eps): 

    iterations = 0              # кол-во итераций алгоритма 
    f_calculations = 2          # кол-во вычислений ф-ии

    phi = (3 - sqrt(5)) / 2     # константа золотого сечения

    # Нулевой этап
    x1 = a + phi * (b - a)      # Точка золотого сечения отрезка [a, x2] 
    x2 = b - phi * (b - a)      # Точка золотого сечения отрезка [x1, b]

    F1 = f(x1)                  # Значения ф-ии в этих точках
    F2 = f(x2)  

    while (b - a >= eps): 
        if (F1 > F2):           # Сравниваем F1 и F2 и отбрасываем одну из частей отрезка
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
            F1 = F2
            F2 = f(x2)          # Считаем значение ф-ии в новой точке (только 1 раз за итерацию!!)

        else:
            b = x2
            x2 = x1
            x1 = a + (b - x2)
            F2 = F1
            F1 = f(x1)

        iterations += 1         # Увеличиваем счётчики
        f_calculations += 1

        # print(f"{iterations} итерация: отрезок [{a}, {b}]")

    return (a+b)/2, iterations, f_calculations

# ----------------------------------------------------------------------

# Метод Фибоначчи
def Fibonacci(f, a, b, eps): 
   
    iterations = 0                          # кол-во итераций алгоритма 
    f_calculations = 2                      # кол-во вычислений ф-ии

    # Вычисление n-го числа Фибоначчи
    phi = (1 + sqrt(5)) / 2                 # константа золотого сечения
    Fib = lambda n: (phi ** n - (1 - phi) ** n) / (2 * phi -1)

    # Определение n (числа вычислений ф-ии)
    n = 1
    s = (b - a) / eps                       # новая переменная, чтобы уменьшить кол-во вычислений 
    while (Fib(n) <= s):
        n += 1

    # Начальный этап
    x1 = a + Fib(n-2) / Fib(n) * (b - a)
    x2 = a + Fib(n-1) / Fib(n) * (b - a)

    # Определим константу различимости между x1 и x2 (чтобы не было самопересечений)
    delta = eps 

    F1 = f(x1)                            
    F2 = f(x2)

    for k in range(1, (n-1) + 1):
        # Алгоритм без последнего шага
        if (k != n-1):
            if (F1 > F2):                   # Сравниваем F1 и F2 и отбрасываем одну из частей отрезка
                a = x1
                x1 = x2
                x2 = a + Fib(n-k-1) / Fib(n-k) * (b - a)
                F1 = F2
                F2 = f(x2)                  # Считаем значение ф-ии в новой точке (только 1 раз за итерацию!!)

            else:
                b = x2
                x2 = x1
                x1 = a + Fib(n-k-2) / Fib(n-k) * (b - a)
                F2 = F1
                F1 = f(x1)
        # Последний шаг
        else:
            x2 = x1 + delta
            F2 = f(x2)
            if (F1 == F2):
                a = x1
            elif (F1 < F2):
                b = x2

        iterations += 1                     # Увеличиваем счётчики
        f_calculations += 1

        # print(f"{iterations} итерация: отрезок [{a}, {b}]")
    
    return (a+b)/2, iterations, f_calculations

# ----------------------------------------------------------------------

# Метод парабол
def Parabolas(f, a, b, eps): 

    f1 = f(a)
    f3 = f(b)

    x = a + 0.5 * (b-a)                     # TODO проверка на (f2 < f1) and (f2 < f3)) в общем случае
    f2 = f(x)

    u_prev = x

    iterations = 0                          # кол-во итераций алгоритма 
    f_calculations = 3                      # кол-во вычислений ф-ии
    
    # Выберем точку x внутри отрезка таким образом, чтобы (f2 < f1) and (f2 < f3)
    # while True:
    #     x = a + random.random() * (b - a)
    #     f2 = f(x)
    #     f_calculations += 1 
    #     if (f2 < f1) and (f2 < f3):
    #         break

    while (b - a >= eps):
        # Найдем точку минимума апроксимирующей квадр. ф-ии
        u = x - ((x - a) ** 2 * (f2 - f3) - (x - b) ** 2 * (f2 - f1)) / (2 * ((x - a) * (f2 - f3) - (x - b) * (f2 - f1)))
        fu = f(u)
        iterations += 1
        f_calculations += 1

        # Выход из цикла (завершение поиска MIN)
        if abs(u - u_prev) <= eps:
            break

        if (u > x):                              
            if (fu < f2):
                a = x
                x = u
                f1 = f2
                f2 = fu
            else:
                b = u
                f3 = fu
        else:
            if (fu < f2):
                b = x
                x = u
                f3 = f2
                f2 = fu
            else:
                a = u
                f1 = fu

        u_prev = u
        # print(f"{iterations} итерация: [{a}, {x}, {b}]")

    return u, iterations, f_calculations

# ----------------------------------------------------------------------

# Метод Брента

# [a,b] - текущий интеравла поиска решения
# х - точка, соответствующая наименьшему значению ф-ии
# w - точка, соответствующая второму снизу значению ф-ии
# v - предыдущее значение w
# Аппроксимирующая парабола строится с помощью трех наилучших точек x, w, v (в случае, если эти 3 точки различны и значения в них также различны)
# u - точка минимума аппроксимирующй параболы 
# Она принимается в качестве след. точки оптимизационного процесса: 
    # если u попадает внутрь интервала [a, c] и отстоит от границ интервала не менее, чем на ε
    # u отстоит от точки х не более, чем на половину от длины предпредыдущего шага
# Если точка u отвергается, то следующая точка находится с помощью золотого сечения большего из интервалов [a, x] и [x, c].

def Brent(f, a, b, eps): 

    sign = lambda z: 1 if z > 0 else (-1 if z < 0 else 0)

    iterations = 0                          # кол-во итераций алгоритма 
    f_calculations = 1                      # кол-во вычислений ф-ии

    K = (3-sqrt(5)) / 2                     # константа Золотого сечения                        
    x = w = v = (a + b) / 2
    Fx = Fw = Fv = f(x)
    e = d = b - a
    
    while (b - a >= eps):
        iterations += 1
        g = e
        e = d
        parabola_accepted = False
        if (x != w) and (x != v) and (v != w) and (Fx != Fw) and (Fw != Fv) and (Fv != Fx):
            u = x - ((x - v) ** 2 * (Fx - Fw) - (x - w) ** 2 * (Fx - Fv)) / (2 * ((x - v) * (Fx - Fw) - (x - w) * (Fx - Fv)))

            if (a+eps <= u <= b-eps) and (abs(u-x) < g/2):
                parabola_accepted = True

                if abs(u-x) < eps:
                    u = x + sign(u-x) * eps
                d = abs(u-x)

        if not parabola_accepted:
            if x < (a+b)/2:
                u = x + K * (b - x)         # Золотое сечение [x, b]
                e = b - x
                d = u - x
            else:
                u = x - K * (x - a)         # Золотое сечение [a, x]
                e = x - a
                d = x - u

        Fu = f(u)
        f_calculations += 1
        if Fu <= Fx:
            if u >= x:
                a = x
            else:
                b = x
            v = w
            w = x
            x = u
            Fv = Fw
            Fw = Fx
            Fx = Fu
        else:
            if u >= x:
                b = u
            else:
                a = u

            if (Fu <= Fw) or (w == x):
                v = w
                w = u
                Fv = Fw
                Fw = Fu
            elif (Fu <= Fv) or (v == x) or (v == w):
                v = u
                Fv = Fu
    return (a+b)/2, iterations, f_calculations