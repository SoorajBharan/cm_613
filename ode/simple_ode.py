import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def dydx_return(y,t):
    return (-y*t + 13)

t = np.linspace(0,5)

y0 = [0,1,2]

y=odeint(dydx_return,y0,t)

plt.plot(t,y)
plt.grid()
plt.show()
