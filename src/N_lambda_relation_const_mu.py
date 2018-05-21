import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.005)

s = (t/0.25)/(1-t/0.25)
z = (t/0.50)/(1-t/0.50)
x = (t/0.75)/(1-t/0.75)

plt.plot(t, s, label = u'μ = 0.25')
plt.plot(t, z, label = u'μ = 0.50')
plt.plot(t, x, label = u'μ = 0.75')

plt.xlim(0,1)
plt.ylim(0, 25)

plt.xlabel('λ')
plt.ylabel('N')

plt.xticks([0.1 * i for i in range(11)])
plt.yticks([1 * i for i in range(26)])

plt.grid(True)
plt.legend()

plt.savefig('N_lambda_relation_const_mu.png', dpi = 300)

plt.show()