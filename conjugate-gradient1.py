import numpy as np
A = np.array([[3, -1, 1], [-1, 6, 2], [1, 2, 7]])
b = np.array([1, 0, 4])
# initial guess
x0 = np.array([0, 0, 0])
# orthohonal vectors
v1 = np.array([1, 0, 0])
v2 = np.array([1/3, 1, 0])
# transpose the matrix
v1_transpose = np.transpose(v1)
v2_transpose = np.transpose(v2)
# calculate the true solution
x_true = np.linalg.solve(A, b)
# first iteration (k=0)
r0 = b- np.dot(A, x0)
alpha0 = np.dot(v1_transpose, r0) / np.dot(v1_transpose, np.dot(A, v1))
x1 = x0 + alpha0 * v1
r1 = r0 - np.dot(A, x1) 
# second iteration (k=1)
beta1 = np.dot(v2_transpose, r1) / np.dot(v2_transpose, np.dot(A, v2))
x2 = x1 + beta1 * v2
# relative error using l_infinity norm
rel_error = np.linalg.norm(x2 - x_true, np.inf) / np.linalg.norm(x_true, np.inf)
print("x1:", x1)
print("x2:", x2)
print("relative error:", rel_error)