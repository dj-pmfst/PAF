import SolarSystem as ss 
import matplotlib.pyplot as plt 
import numpy as np 

zemlja = ss.Object(5.9742 * 10**24, np.array((0, -29783)), np.array((-1*1.496 * 10**11, 0)), "blue")
sunce = ss.Object(1.989 * 10**30, np.array((0, 0)), np.array((0, 0)), "yellow")

a = ss.Orbit(365.242 * 24 * 3600)
a.add_object(sunce)
a.add_object(zemlja)

a.plot()