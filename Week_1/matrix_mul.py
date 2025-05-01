# Define matrices
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

# Initialize result matrix with zeros
result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

# Perform multiplication
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("Product (A x B):")
for row in result:
    print(row)
