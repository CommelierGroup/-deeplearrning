import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([[2, 0], [1, 3], [3, 1], [0, 2]])

result = a @ b # == np.dot(a, b)
print(result)
