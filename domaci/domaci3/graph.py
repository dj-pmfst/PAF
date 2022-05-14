import matplotlib.pyplot as plt 

a = []
v = []
x = []
t = []
lista = []

with open ('podaci.txt', 'r') as fh:
    for line in fh:
        lista.append(line.rstrip().split(","))

for el in lista:
    a.append(float(el[0]))
    v.append(float(el[1]))
    x.append(float(el[2]))
    t.append(float(el[3]))

plt.plot(t, x)
plt.show()

plt.plot(t, v)
plt.show()

plt.plot(t, a)
plt.show()