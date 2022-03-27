import particle as prt 

p1 = prt.particle(0.01)
p1.set_initial_conditions(10, 0, 0, 30)
p1.range()
p1.analytical()
a = p1.error()
p1.plot_trajectory()

print("Odstupanje je", a ,"%")