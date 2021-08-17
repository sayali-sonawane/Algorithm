# a = []
# count = 0
# for i in range(1000):
#     if i %3 == 0:
#         a.append(-1*i)
#         count += 1
#     else:
#         a.append(i)
# print(a)
# print(count)

import time

tic = time.time()
for i in range(10**10):
    a = 1+2
toc = time.time()

print(toc - tic)