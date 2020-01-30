import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2020)
arr_0 = list(10 + 5*np.random.rand(20, 1))
arr_1 = list(10 + 5*np.random.rand(20, 1))
arr_2 = list(10 + 5*np.random.rand(20, 1))
arr_3 = list(10 + 5*np.random.rand(20, 1))
rpms = np.linspace(0, 2500, len(arr_0))

figure = plt.figure()
plt.plot(rpms, arr_0, ls='-')
plt.plot(rpms, arr_1, ls='--')
plt.plot(rpms, arr_2, ls=':')
plt.plot(rpms, arr_3, ls='-.')
plt.show()

