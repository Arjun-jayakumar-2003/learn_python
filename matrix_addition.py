import numpy as np
print("Matrix Multiplications")
print("_______________________")
rows1 = int(input("Enter the size of rows for first matrix: "))
columns1 = int(input("Enter the size of columns for first matrix: "))
matrix1 = np.zeros((rows1, columns1))
print("The first matrix entered by you is: ")
for i in range(rows1):
    for j in range(columns1):
        matrix1[i, j] = int(input(f"Enter the element for the row {i + 1} and column {j + 1}: "))

rows2 = int(input("Enter the size of rows for second matrix: "))
columns2 = int(input("Enter the size of columns for second matrix: "))
matrix2 = np.zeros((rows2, columns2))

for i in range(rows2):
    for j in range(columns2):
        matrix2[i, j] = int(input(f"Enter the element for the row {i + 1} and column {j + 1}: "))

matrix_addition = matrix1 + matrix2

print("The resultant matrix after addition is\n ", matrix_addition)
