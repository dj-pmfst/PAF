import numpy as np
import math

def derivacija_tocka(f, x, dx=0.01, m=3):
    if m == 2 :
        return((f(x+dx)-f(x))/dx)
    else: 
        if m == 3 :
            return((f(x+dx)-f(x-dx))/2*dx)

def derivacija(f, a, b):
    fx_lista = []
    x = np.linspace(a, b, 100)
    for i in x:
        fx_lista.append(derivacija_tocka(f, i))
    return x, fx_lista

def integral(f, a, b, N):
    gornja = 0
    donja = 0
    dx = (b-a)/N
    x = np.linspace(a, b, int(N+1))
    for i in range(len(x)-1):
        gornja+=(f(i)*dx)
        donja+=(f(i+1)*dx)
    return gornja, donja

def integral_t(f, a, b, N):
    s = 0
    dx = (b-a)/N
    x = np.linspace(a, b, int(N+1))
    for i in range(len(x)-1):
        s +=(f(x[i]) + (f(x[i+1]) - f(x[i]))/2)*(dx)
    return s
