import numpy as np
from scipy import sparse
a = np.array([[1, 2], [3, 5]])
b = np.array([3, 5])
x = np.linalg.solve(a, b)
print(x)
print(np.allclose(np.dot(a, x), b))