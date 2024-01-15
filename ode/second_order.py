""" 
The second order eqaution to be solved is of the following 
(d^2y/dx^2) + 2*(dy/dx) + 2y = cos(2x)
y(0) = 0
dy/dx = 0 
x range = linspace(0,10,200)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

"""
v = [v0 , v1]
v0 = y
v1 = dy/dy 
dv/dx = cos(2x) - 2(dy/dx) - 2y
      = cos(2x) - 2 v1 - 2 v0
"""
def dydx(v,x):
    return(v[1],np.cos(2*x)-(2*v[1])-(2*v[0]))

y0 = [0,0]

x = np.linspace(0,10,200)

y = odeint(dydx,y0,x)

plt.plot(x,y[:,0],label="Solution")
plt.plot(x,y[:,1],label="Fisrt Derivative")
plt.legend()
plt.grid()
plt.show()
