import numpy as np
# Define two matrices
matrix1 = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
matrix2 = np.array([[9, 8, 7],
[6, 5, 4],
[3, 2, 1]])
# Matrix Addition
result_addition = np.add(matrix1, matrix2)
# Matrix Multiplication
result_multiplication = np.dot(matrix1, matrix2)
# Print the original matrices and results
print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nMatrix Addition (Matrix1 + Matrix2):")
print(result_addition)
print("\nMatrix Multiplication (Matrix1 * Matrix2):")
print(result_multiplication)
