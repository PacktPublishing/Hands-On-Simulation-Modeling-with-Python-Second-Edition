import numpy as np
import matplotlib.pyplot as plt

np.random.seed(4)

n = 1000

sqn = 1/np.math.sqrt(n)

z_values = np.random.randn(n)

Yk = 0

sb_motion=list()

for k in range(n):
    Yk = Yk + sqn*z_values[k]
    sb_motion.append(Yk)

plt.plot(sb_motion)
plt.show()
