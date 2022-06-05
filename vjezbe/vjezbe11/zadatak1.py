import SolarSystem as ss 
import matplotlib.pyplot as plt 
import numpy as np 

zemlja = ss.Object(5.9742 * 10**24, np.array((0, 29783)), np.array((0, 1.486 * 10**11)))
sunce = ss.Object(1.989 * 10**30, np.array((0,0)), np.array((0,0)))

a = ss.Orbit(zemlja, sunce, 365.242 * 24 * 3600)

a.plot()