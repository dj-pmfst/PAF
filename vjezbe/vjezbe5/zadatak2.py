import harmonic_oscillator as ho 
import matplotlib.pyplot as plt 

p1 = ho.har_osc()
p1.set_initial_conditions(10, 100, 0, 10, 3, 0.01)
p2 = ho.har_osc()
p2.set_initial_conditions(10, 100, 0, 10, 3, 0.1)

p1.oscillate()
p2.oscillate()

a, b = p1.period(3)
c, d = p2.period(3)
e, f = p1.period_analytical(3)

plt.scatter(a, b, s = 2)
plt.scatter(c, d, s = 2, color = "green")
plt.plot(e, f, color = "red")
plt.show()