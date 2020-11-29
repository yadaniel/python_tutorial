#!/cygdrive/c/Python37/python

import pdb
import math, cmath
import numpy as np
import control as c
import control.matlab as cm
from matplotlib import pylab as plt

s1 = c.tf(1,[1,1])
s2 = c.feedback(c.series(s1,s1),1,-1)
t1,y1 = c.step_response(s2)

s3 = c.tf(1,[1,2,2])
t2,y2 = c.step_response(s3)

# 1/(s+1) * 1/(s+1) = 1/(s**2+2*s+1) => G(s)
# forward sysem A, negative feedback system B => A/(1+A*B)
# G(s)/(1+G(s)) = 1/(s**2+2*s+2)

plt.subplot(2,1,1)
plt.plot(t1,y1)
plt.grid()

plt.subplot(2,1,2)
plt.plot(t2,y2)
plt.grid()

plt.show()

