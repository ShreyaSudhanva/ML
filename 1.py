import numpy as np
from scipy import sparse

vector_row = np.array([1, 2, 3])
print(vector_row)

vector_column = np.array([[1],
                          [2],
                          [3]])
print(vector_column)
matrix = np.array([[0, 0],
                   [0, 1],
                   [3, 0]])
print(matrix)
print(matrix.shape)
print(matrix.size)

matrix_object = np.mat([[1, 2],
                        [1, 2],
                        [1, 2]])


matrix_sparse = sparse.csr_matrix(matrix)
print(matrix_sparse)

print((matrix+100))
print('mean=',np.mean(matrix))
print('variance=',np.var(matrix))
print('SD=',np.std(matrix))
print('Transpose=',matrix.T)