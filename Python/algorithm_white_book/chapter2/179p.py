class SquareMatrix:
    def __init__(self, n, values=None):
        self.n = n  # The size of the matrix (n x n)
        if values is None:
            self.values = [[0] * n for _ in range(n)]
        else:
            self.values = values

    def __mul__(self, other):
        if isinstance(other, SquareMatrix):
            # Matrix multiplication
            result = SquareMatrix(self.n)
            for i in range(self.n):
                for j in range(self.n):
                    result.values[i][j] = sum(self.values[i][k] * other.values[k][j] for k in range(self.n))
            return result
        else:
            raise ValueError("Can only multiply by another SquareMatrix.")

    def identity(self):
        # Create an identity matrix of the same size
        identity_matrix = SquareMatrix(self.n)
        for i in range(self.n):
            identity_matrix.values[i][i] = 1
        return identity_matrix

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.values])


# Example: Creating a 2x2 matrix
A = SquareMatrix(2, [[1, 2], [3, 4]])

# Power function for matrix exponentiation
def pow(A, m):
    if m == 0:
        return A.identity()
    if m % 2 == 0:
        half = pow(A, m // 2)
        return half * half
    else:
        return pow(A, m - 1) * A


# Example usage
A = SquareMatrix(2, [[1, 2], [3, 4]])
result = pow(A, 3)
print(result)
