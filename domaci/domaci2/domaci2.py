import kinematics as knm 

def f_const(v, x, t):
    return 30

def f_osc(v, x, t):
    return -30*x

a = knm.kinematics()
a.set_initial_conditions(f_const, 0, 0, 3, 3)
a.move()

a2 = knm.kinematics()
a2.set_initial_conditions(f_osc, 0, 1, 3, 3)
a2.move()

a.graph()
a2.graph()