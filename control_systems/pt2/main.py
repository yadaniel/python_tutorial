#!/cygdrive/c/Python37/python

import pdb
import math, cmath
import numpy as np
import control as c
import control.matlab as cm
from matplotlib import pylab as plt

# import pyqtgraph as pg
# import pyqtgraph.examples as pge
# #
# # define the data
# theTitle = "pyqtgraph plot"
# y = [2,4,6,8,10,12,14,16,18,20]
# x = range(0,10)
# #
# # create plot
# plt = pg.plot(x, y, title=theTitle, pen='r')
# plt.showGrid(x=True,y=True)
# #
# ## Start Qt event loop.
# if __name__ == '__main__':
#     import sys
#     if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
#         pg.QtGui.QApplication.exec_()
# # pge.run()

# x[i] != 0 between X1 and X2
# y[i] != 0 between Y1 and Y2
# z[n] = sum(k=-inf to n) { x[k]*y[n-k] }
# with given ranges for non zero values
# z[n] = sum(k=X1 to n) { x[k]*y[n-k] }
# in general for x[] => X1 < k < X2
# in general for y[] => Y1 < n-k < Y2
# Y1 < n - k => Y1 + k < n
# Y2 > n - k => Y2 + k > n
# Y1 + k < n < Y2 + k, with X1 < k < X2
# Y1 + X1 < n < Y2 + X2
# e.g.
# x = np.array([0,0,1,0,0]) => len(x) = 5 ... range 0 to 4
# y = np.array([0,0,0,1,0,0,0]) => len(y) = 7 ... range 0 to 6
# z = np.convolve(x,y) => len(z) => 11 ... range 0+0 ... 4+6


def faltung(x1,x2):
    n1, n2 = len(x1), len(x2)
    n3 = n1 + n2 - 1    # 0+0 ... n1-1+n2-1=n1+n2-2, but len()=n1+n2-1
    y = np.zeros(n3, dtype=np.int32)
    for n in range(n3):
        y[n] = sum([x1[i]*x2[n-i] for i in range(n1) if 0<(n-i)<n2])
    return y

x = np.array([0,0,1,0,0])
y = np.array([0,0,0,1,0,0,0])
z = np.convolve(x,y)
z1 = faltung(x,y)
np.set_printoptions(linewidth=80)
print(z)
print(z1)

s1 = c.tf(1, [1,1])
N = 1000
t = np.linspace(0,10,N)
# x = np.sin(2*math.pi*1.5*t)
x = np.ones(N)
y,t1,x1 = cm.lsim(s1, x, t)
# pdb.set_trace()


f = plt.figure(0)
#
plt.subplot(211)
plt.plot(t,x)
plt.grid()
plt.title("input")
#
plt.subplot(212)
plt.plot(t,y)
plt.grid()
plt.title("output")
#
plt.show()

