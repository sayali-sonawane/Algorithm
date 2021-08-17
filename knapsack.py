import sys


def knapsack(val, wt, W, n):
    K = [[0 for j in range(len(wt) + 1)] for i in range(W + 1)]

    for j in range(1, len(wt) + 1):
        for i in range(1, W + 1):
            if wt[j-1] > i:
                K[i][j] = K[i][j - 1]
            else:
                K[i][j] = max(K[i-wt[j-1]][j - 1]+val[j-1], K[i][j - 1])

    return K[W][n]


def main():
    val = [60, 100, 120, 400]
    wt = [10, 20, 30, 40]
    W = 50
    n = len(val)
    print(knapsack(val, wt, W, n))



if __name__ == '__main__':
    main()
