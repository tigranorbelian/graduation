import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.005)

s = t/(1-t)
z = t**2/(1-t)

plt.plot(t, s, label = u'Система')
plt.plot(t, z, label = u'Накопители')

plt.xlim(0,1)
plt.ylim(0, 10)

plt.xlabel('ρ')
plt.ylabel('N')

plt.xticks([0.1 * i for i in range(11)])
plt.yticks([1 * i for i in range(11)])

plt.grid(True)
plt.legend()

plt.savefig('N_S_amp_amp_D_ro_relation.png', dpi = 300)

plt.show()