# Uğur Dinçer

import numpy as np
import matplotlib.pyplot as plt
import time

started = time.time()

# System Matrices
A = np.array([[0, 1], [0, 0]])
B = np.array([[0], [1]])

# Controller Gain
K = np.array([-2, -2])

# Finding P such that A'*P+P*A + Q = 0
P = np.array([[1.2500, 0.2500], [0.2500, 0.3750]])

# System Parameters
m = 1
c = 2
k = 3

# Initial Values
x = np.array([[0], [5]])
gammaHat = np.array([[0], [0]])

# Time Constants
dt = 0.0001
T = 50

# Real System Parameters
gamma = np.array([[k/m], [c/m]])

x1 = []

for t in np.arange(0, T, dt):
    # Stabilizing Input
    u = np.dot(K, x) - np.dot(np.transpose(gammaHat), x)

    # State Space Form
    dot_x = np.dot(A, x) + np.dot(B, (np.dot(np.transpose(gamma), x) + u))

    temp = np.dot(np.dot(np.transpose(B), P), x)

    dot_gammaHat = np.dot(x, temp)

    # Iterating
    x = x + dot_x * dt
    gammaHat = gammaHat + dot_gammaHat * dt

    x1.append(x[0])


plt.plot(np.arange(0, T, dt), x1)
plt.show()

ended = time.time()
print("Elapsed time => ", ended - started)
