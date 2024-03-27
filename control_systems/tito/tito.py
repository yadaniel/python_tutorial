#!C:/PYthon3/python

import sys
import numpy as np
import control
import matplotlib.pyplot as plt

# Define transfer functions for the TITO
G11 = control.TransferFunction([1], [1, 1],     inputs="u1", outputs="y1_u1")
G12 = control.TransferFunction([0.5], [1, 2],   inputs="u2", outputs="y1_u2")
G21 = control.TransferFunction([0.8], [1, 3],   inputs="u1", outputs="y2_u1")
G22 = control.TransferFunction([1], [1, 2],     inputs="u2", outputs="y2_u2")

Y1_sum = control.summing_junction(inputs=["y1_u1","y1_u2"], outputs="y1")
Y2_sum = control.summing_junction(inputs=["y2_u1","y2_u2"], outputs="y2")

plant = control.interconnect([G11, G12, G21, G22, Y1_sum, Y2_sum], inputs=["u1","u2"], outputs=["y1","y2"])
plant_ = control.c2d(plant, 0.001, "zoh")
# print(plant)
# print(plant_)
# sys.exit()

# Design PID Controllers
Kp1 = 1.0
Ki1 = 0.1

Kp2 = 0.8
Ki2 = 0.08

# Define PID Controllers manually
pid1 = control.TransferFunction([Kp1,Ki1], [1,0], inputs="e1", outputs="u1")
pid2 = control.TransferFunction([Kp2,Ki2], [1,0], inputs="e2", outputs="u2")

E1_sum = control.summing_junction(inputs=["r1","-y1"], outputs="e1")
E2_sum = control.summing_junction(inputs=["r2","-y2"], outputs="e2")

s1 = control.interconnect([E1_sum, E2_sum, pid1, pid2, plant], inputs=["r1","r2"], outputs=["y1","y2"])
# s2 = control.c2d(s1, 0.001, "zoh")
print(s1)

t11, y11 = control.step_response(s1[0,0])
t12, y12 = control.step_response(s1[0,1])
t21, y21 = control.step_response(s1[0,1])
t22, y22 = control.step_response(s1[1,1])

f = plt.figure()

plt.subplot(2,2,1)
plt.grid()
plt.plot(t11, y11)

plt.subplot(2,2,2)
plt.grid()
plt.plot(t12, y12)

plt.subplot(2,2,3)
plt.grid()
plt.plot(t21, y21)

plt.subplot(2,2,4)
plt.grid()
plt.plot(t22, y22)

plt.show()

