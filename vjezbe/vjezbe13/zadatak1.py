import Universe as u
import matplotlib.pyplot as plt 
import numpy as np

au = 1.496 * 10**11

sunce = u.Object(1.989 * 10**30, np.array((0, 0)), np.array((0, 0)), "yellow")
zemlja = u.Object(5.9742 * 10**24, np.array((-1*au, 0)), np.array((0, -29783)), "blue")
merkur = u.Object(3.3 * 10**24, np.array((0, 0.466*au)), np.array((-47362, 0)), "brown")
venera = u.Object(4.8685*10**24, np.array((0.723*au, 0)), np.array((0, 35020)), "orange")
mars = u.Object(6.417*10**23, np.array((0, -1.666*au)), np.array((24007, 0)), "red")
komet = u.Object(10e14, np.array((5*au, -au)), np.array((np.cos(np.pi/3)*16000), np.sin(np.pi/3)*16000), "lightblue")

ss = u.SolarSystem(10*365.242*3600*24)

ss.add_object(mars)
ss.add_object(zemlja)
ss.add_object(venera)
ss.add_object(merkur)
ss.add_object(sunce)
ss.add_object(komet)

ss.plot()