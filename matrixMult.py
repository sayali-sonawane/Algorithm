import sys


def matrixMult(dims, i, j, M):
    n = len(dims)

    if i == j:
        return 0

    if M[i][j] != -1:
        return M[i][j]

    M[i][j] = sys.maxsize
    for k in range(i, j):
        M[i][j] = min(M[i][j], matrixMult(dims, i, k, M) + dims[i-1]*dims[j]*dims[k] + matrixMult(dims, k+1, j, M))

    return M[i][j]


dims = [5, 4, 6, 2, 7]
M = [[-1 for i in range(len(dims)+1)] for j in range(len(dims)+1)]
print(matrixMult(dims, 1, len(dims)-1, M))
