def matrix_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matrix_subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matrix_multiply(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def matrix_transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def matrix_determinant(A):
    if len(A) == 1: return A[0][0]
    if len(A) == 2: return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return sum(((-1) ** c) * A[0][c] * matrix_determinant(
        [[A[i][j] for j in range(len(A)) if j != c] for i in range(1, len(A))]) for c in range(len(A)))


def matrix_inverse(A):
    det = matrix_determinant(A)
    if det == 0: raise ValueError("Matriz no invertible")
    n = len(A)
    cofactors = [[((-1) ** (r + c)) * matrix_determinant(
        [[A[i][j] for j in range(n) if j != c] for i in range(n) if i != r]) for c in range(n)] for r in range(n)]
    cofactors = matrix_transpose(cofactors)
    return [[cofactors[i][j] / det for j in range(n)] for i in range(n)]
