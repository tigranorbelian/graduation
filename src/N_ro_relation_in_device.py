import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.005)

s = t**2/(1-t)

plt.plot(t, s)

plt.xlim(0,1)
plt.ylim(0, 20)

plt.xlabel('ρ')
plt.ylabel('N')

plt.xticks([0.1 * i for i in range(11)])
plt.yticks([1 * i for i in range(21)])

plt.grid(True)

plt.savefig('N_ro_relation_in_device.png', dpi = 300)

plt.show()