import bezier
import numpy as np
import matplotlib.pyplot as plt


a = np.array([[1.0, 2.1, 3.0, 4.0, 5.0, 6.0], [0, 1.1, 2.1, 1.0, 0.2, 0]])
curve = bezier.Curve(a, degree=5)
# print(curve)
s_vals = np.linspace(0.0, 1.0, 30)
print(s_vals)
data = curve.evaluate_multi(s_vals)
x33 = data[0]
y33 = data[1]
print(data)
plt.plot(x33, y33, 'y', linewidth=2.0, linestyle="-", label="y2")
plt.show()


# inter_val0 = np.linspace(0, 50, 11, dtype='int')
# inter_val1 = np.linspace(0, 100, 80, dtype='int')
# print(inter_val1)
# print(inter_val1[inter_val0])
