import projectile as pr 
import numpy as np 
import matplotlib.pyplot as plt 

a = pr.ProjectileDrop()
a.set_initial_conditions(200, 2000)
a.target(10, 5, 10)