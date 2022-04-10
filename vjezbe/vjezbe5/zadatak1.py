import harmonic_oscillator as ho 
import matplotlib.pyplot as plt

p1 = ho.har_osc()
p1.set_initial_conditions(10, 100, 0, 10, 3, 0.01)
p2 = ho.har_osc()
p2.set_initial_conditions(10, 100, 0, 10, 3, 0.1)
a, b = p1.analytical()
c, d = p1.oscillate()
e, f = p2.oscillate()
plt.scatter(c, d, s = 2)
plt.scatter(e, f, s = 2, color = "green")
plt.plot(a,b, color = "red")
plt.show()