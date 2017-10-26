# Question: https://www.hackerrank.com/challenges/fibonacci-modified/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
t1, t2, n = input().split()
t1 = int(t1)
t2 = int(t2)
n = int(n)
fib = [0]*n
fib[0] = t1
fib[1] = t2

for i in range(2, n):
    fib[i] = fib[i - 2] + (fib[i - 1]) ** 2
print(fib[n-1])