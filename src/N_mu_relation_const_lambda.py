import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.005)

s = (0.25/t**2)/(1-0.25/t) 
z = (0.50/t**2)/(1-0.50/t)
x = (0.75/t**2)/(1-0.75/t)

plt.plot(t, s, label = u'λ = 0.25')
plt.plot(t, z, label = u'λ = 0.50')
plt.plot(t, x, label = u'λ = 0.75')

plt.xlim(0,1)
plt.ylim(0, 25)

plt.xlabel('μ')
plt.ylabel('N')

plt.xticks([0.1 * i for i in range(11)])
plt.yticks([1 * i for i in range(26)])

plt.grid(True)
plt.legend()

plt.savefig('N_mu_relation_const_lambda.png', dpi = 300)

plt.show()