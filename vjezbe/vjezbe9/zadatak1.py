import BungeeJump as bp 
import matplotlib.pyplot as plt

p1 = bp.BungeeJump()
p1.set_initial_conditions(100, 1.125, 0.45, 10, 100, 1, 20, 25, 0.001)
p1.jump()
p1.plot()

p2 = bp.BungeeJump()
p2.set_initial_conditions(100, 1.125, 0.45, 10, 100, 0, 20, 25, 0.001)
p2.jump()
p2.plot()