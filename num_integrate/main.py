#!/cygdrive/c/Python37/python

from scipy.integrate import odeint, solve_ivp
import matplotlib.pylab as plt
import numpy as np
from math import *

t = np.linspace(0.1, 10, 100)
y = odeint(lambda y,t: log10(t), y0=0, t=t)

# y1 = solve_ivp(lambda t,y: log10(t), t_span=[0.1, 10], y0=[0])
# y1 = solve_ivp(lambda t,y: log10(t), t_span=[0.1, 10], y0=[0], method='LSODA')
# y1 = solve_ivp(lambda t,y: log10(t), t_span=[0.1, 10], y0=[0], method='RK45')
# y1 = solve_ivp(lambda t,y: log10(t), t_span=[0.1, 10], y0=[0], method='RK23')
y1 = solve_ivp(lambda t,y: log10(t), t_span=[0.1, 10], y0=[0], method='DOP853')

f = plt.figure(0)

plt.subplot(211)
plt.plot(t, y)
plt.grid()

plt.subplot(212)
plt.plot(y1.t,y1.y[0])
plt.grid()

plt.show()


