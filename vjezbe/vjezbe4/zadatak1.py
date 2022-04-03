import calculus
import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return x**3 + x**2 + x + 1
def f2(x):
    return np.sin(x)

x1_lista, y1_lista = calculus.derivacija(f1, 1, 2, 0.01)
x2_lista, y2_lista = calculus.derivacija(f1, 1, 2, 0.1)

n = np.linspace(1, 2, 100)
analiticko = []
for i in n:
    analiticko.append(f1(i))

plt.scatter(x1_lista, y1_lista)
plt.scatter(x2_lista, y2_lista)
plt.plot(n, analiticko)
plt.show()