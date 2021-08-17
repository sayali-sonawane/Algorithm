import math
import os
import random
import re
import sys
import copy



def activityNotifications(expenditure, d):
    import bisect

    def median(a):
        n = len(a)
        if n % 2 == 0:
            return (a[int(n / 2)] + a[int(n / 2) - 1]) / 2
        else:
            return a[int(n / 2)]

    notify = 0
    n_exp = len(expenditure)
    arr = copy.deepcopy(expenditure[:d])
    sorted_arr = sorted(arr)
    count = 0
    for i in range(d, n_exp):
        count += 1
        threshold = median(sorted_arr)
        if expenditure[i] >= 2 * threshold:
            notify += 1
        arr.remove(arr[0])
        sorted_arr.remove(arr[0])
        arr.append(expenditure[i])
        bisect.insort(sorted_arr, expenditure[i])
        if notify > 633:
            print(arr)

    print(count)
    return notify


# f = open("/Users/AC55123/Desktop/frad.txt", "r")
#
# expenditure = list(map(int, f.read().rstrip().split()))
#
# # print(expenditure)
# import time
# tic = time.time()
# print(activityNotifications(expenditure, 10000))
# toc = time.time()
# print("time {}".format(toc-tic))

from collections import Counter


# def countTriplets(arr, r):
#     a = Counter(arr)
#     b = Counter()
#     s = 0
#     for i in arr:
#         j = i//r
#         k = i*r
#         a[i]-=1
#         if b[j] and a[k] and i%r == 0:
#             s+=b[j]*a[k]
#         b[i]+=1
#     return s

def countTriplets(arr, r):
    output_count = 0
    counter = Counter(arr)
    prev_vals = Counter()

    for j in arr:
        i = j // r
        k = j * r
        counter[j] -= 1
        if prev_vals[i] and counter[k] and j % r == 0:
            output_count += prev_vals[i] * counter[k]
        prev_vals[j] += 1


    return output_count

from itertools import combinations
# arr = [1 for _ in range(100)]
# arr = [1,2,1,2,4]
# r = 2
# print(countTriplets(arr, r))

from statistics import median
def get_median(count, d):
    if d % 2 == 1:
        idx = 0
        for i in range(len(count)):
            idx += count[i]
            if idx >= d // 2 + 1:
                return 2*i
    if d % 2 == 0:
        idx = 0
        low, high = 0, 0
        for i in range(len(count)):
            idx += count[i]
            if idx > d // 2 + 1 and not low and not high:
                return i * 2
            if idx == d // 2 and not low:
                low = i
            elif idx >= d // 2 + 1 and not high and low:
                high = i
                return low + high
            elif idx == d // 2 + 1 and not high and not low:
                return 2*i



def activityNotifications(expenditure, d):
    count = [0 for _ in range(201)]
    notify = 0

    for i in expenditure[:d]:
        count[i] += 1

    start = 0
    for i in expenditure[d:]:
        # med = median(expenditure[start:start+d])
        if i >= get_median(count, d):
        # if i >= med*2:
            notify += 1
        count[i] += 1
        count[expenditure[start]] -= 1
        start += 1

    return notify

# arr = [10,20,30,40,50]
# d = 4

# f = open("/Users/AC55123/Desktop/frad.txt", "r")
# #
# arr = list(map(int, f.read().rstrip().split()))
# d = 10000
# print(activityNotifications(arr, d))


def countInversions(arr):
    # swaps = 0
    def mergeSort(myList):
        swaps, swap1, swap2 = 0, 0, 0
        if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]

            # Recursive call on each half
            swap1 = mergeSort(left)
            swap2 = mergeSort(right)

            # Two iterators for traversing the two halves
            i = 0
            j = 0

            # Iterator for the main list
            k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    # The value from the left half has been used
                    myList[k] = left[i]
                    # Move the iterator forward
                    i += 1
                else:
                    swaps += 1
                    myList[k] = right[j]
                    j += 1
                # Move to the next slot
                k += 1

            # For all the remaining values
            while i < len(left):
                # swaps += 1
                myList[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                myList[k] = right[j]
                j += 1
                k += 1
        return swaps + swap1 + swap2

    swaps = mergeSort(arr)
    return swaps

print(countInversions([8, 3, 2, 4]))


def isValid(s):
    freq = Counter(s)
    counter_freq = Counter()
    for k, v in freq.items():
        counter_freq[v] += 1

    if len(counter_freq) > 2:
        return "NO"
    if len(counter_freq) == 1:
        return "YES"

    common_freq = 0
    freq_freq = 0
    for k, v in counter_freq.items():
        if v > freq_freq:
            freq_freq = v
            common_freq = k

    keys = list(counter_freq.keys())
    keys.remove(common_freq)
    other_freq = keys[0]

    if (other_freq == 1 or other_freq == common_freq + 1) and counter_freq[other_freq] == 1:
        return "YES"

    # val_list = list(counter_freq.values())
    # if val_list[0] >= val_list[1] and val_list[1] > 1:
    #     return "NO"
    # elif val_list[1] >= val_list[0] and val_list[0] > 1:
    return "NO"

# print(isValid("aabbcd"))


def substrCount(n, s):
    sub_dict = {}

    def isSubstr(s, j, l, sub_dict):
        sub = s[j:j + l]
        if l % 2 == 0 and len(set(list(s))) == 1:
            return True
        if l % 2 == 1:
            if (j + 1, j + l - 2) in sub_dict:
                if s[j] == s[j + l - 1] and s[j] == s[j + 1]:
                    return True
            else:
                for i in range(int(l / 2)):
                    if sub[i] == sub[l - i - 1] and sub[i] == sub[0]:
                        continue
                    else:
                        return False
                return True
        return False

    count = n
    for l in range(2, n + 1):
        for j in range(0, n - l + 1):

            if isSubstr(s, j, l, sub_dict):
                sub_dict[(j, j + l - 1)] = 1
                count += 1
    return count

# print(substrCount(5, "asasd"))


def maxMin(k, arr):
    if len(arr) == 0 or len(arr) < k:
        return 0
    if k == 1:
        return min(arr)
    # Write your code here
    arr = sorted(arr)
    min_diff = math.inf
    for i in range(len(arr) - k + 1):
        diff = abs(arr[i] - arr[i + k - 1])
        if diff < min_diff:
            min_diff = diff

    return min_diff

# print(maxMin(3, [100,200,300,350, 400,401, 402]))


def reverse(s):
    l = len(s)
    for i in range(l//2):
        if i == l-1-i:
            continue
        s[i], s[l-1-i] = s[l-1-i], s[i]

    return s

    # Write your code here
def reverseShuffleMerge(s):
    # Write your code here
    s = list(s)
    s = reverse(s)
    sorted_char = []
    count = Counter(s)
    for k, v in count.items():
        count[k] = v // 2
    ref_count = Counter(s)
    for k, v in ref_count.items():
        ref_count[k] = v // 2

    for k, v in count.items():
        for i in range(v):
            sorted_char.append(k)
    sorted_char = sorted(sorted_char)
    # visited = sorted(sorted_char)

    actual = []
    shuffled = []
    j = 0
    for i in s:
        lookup = sorted_char[j]
        if (i <= lookup and count[i] > 0) or (ref_count[i] == 0):
            actual.append(i)
            count[i] -= 1
            # visited.remove(i)
            # sorted_char.remove(sorted_char[0])
            if j < len(sorted_char)-1:
                j += 1
        else:
            shuffled.append(i)
            ref_count[i] -= 1

    a = ""
    for i in actual:
        a += str(i)

    return a

# print(reverseShuffleMerge("djjcddjggbiigjhfghehhbgdigjicafgjcehhfgifadihiajgciagicdahcbajjbhifjiaajigdgdfhdiijjgaiejgegbbiigida"))


def whatFlavors(cost, money):
    # creating index dict
    ind_dict = {}
    for i, v in enumerate(cost):
        if v in ind_dict:
            ind_dict[v].append(i + 1)
        else:
            ind_dict[v] = [i + 1]

    cost = sorted(cost)

    for i in range(len(cost)):
        k = money - cost[i]
        if money - cost[i] in ind_dict:
            first = ind_dict[cost[i]][0]
            ind_dict[cost[i]].pop(0)
            second = ind_dict[money - cost[i]][0]
            mini = first if first < second else second
            maxi = first if first > second else second
            print("{} {}".format(mini, maxi))
            return

# whatFlavors([7, 2, 5, 4, 11], 12)

def binarySearch(arr, i, j, k):
    n = len(arr)
    if n == 1 and arr[0] == k:
        return True, i
    elif n == 1 and arr[0] > k:
        return False, i
    elif n == 1 and arr[0] < k:
        return False, i+1

    if arr[n // 2] == k:
        return True, (j + i) // 2
    elif arr[n // 2] > k:
        return binarySearch(arr[:n // 2], i, (j + i) // 2, k)
    elif arr[n // 2] < k:
        return binarySearch(arr[n // 2 + 1:], (j + i) // 2 + 1, j, k)


def triplets(a, b, c):
    count = 0
    a, b, c = sorted(list(set(a))), sorted(list(set(b))), sorted(list(set(c)))

    lena, lenb, lenc = len(a), len(b), len(c)

    for ib in range(lenb):
        w, x = binarySearch(a, 0, lena, b[ib])
        y, z = binarySearch(c, 0, lenc, b[ib])
        a_val = x+1 if w else x
        c_val = z+1 if y else z
        count += a_val * c_val

    return count


# a = [1,3,5,7]
# b = [5,7,9]
# c = [7,9,11,13]
# print(triplets(a, b, c))

# print(binarySearch([7,9,11,13], 0, 4, 14))

def calc(d, machines):
    items = 0
    for m in machines:
        items += d // m
    return items


def recur(days, machines, goal):
    mid = len(days)//2
    day = []
    items = calc(days[mid], machines)

    if items == goal:
        day.append(days[mid])
    if len(days) == 1:
        return day
    if items >= goal and len(days) > 1:
        return day + recur(days[:mid], machines, goal)
    elif items <= goal and len(days) > 1:
        return day + recur(days[mid:], machines, goal)
    return day


def minTime(machines, goal):
    items = 0
    maxi = (min(machines) * goal)
    mini = len(machines)

    days = [i for i in range(mini,maxi)]

    return min(recur(days, machines, goal))


# input = "1386 95 2944 4740 3903 4224 2078 3145 4079 329 2735 510 335 138 1452 4439 4280 1886 416 778 2240 4381 3002 963 975 528 2001 4620 2575 3013 2578 312 3107 521 1403 3361 4744 3480 1505 174 3808 591 683 494 2080 3487 4932 1359 372 1699 3488 2612 2432 1489 4926 3406 3369 3278 4377 2295 1290 1954 2606 748 3827 4009 4108 4922 3840 1964 1448 2648 2555 3482 3141 4634 1968 4425 2345 2340 2475 832 1303 4906 3673 2580 3311 2041 858 2687 4335 2147 993 3292 4247 1171 3652 3354 1092 2492 1670 3891 1491 576 2373 983 1561 4340 1759 3905 3031 586 4737 685 491 4761 3265 154 1801 4122 4192 2487 2620 184 2130 1866 2706 782 1572 150 4625 3241 4040 2467 3816 2764 4801 376 3456 1560 633 1486 2145 369 3523 3987 129 1787 4140 3281 908 3332 767 4879 4867 2896 1745 3925 29 3316 4074 1005 1556 4465 3471 1723 2229 3272 3450 684 1183 4082 3521 4679 802 2043 3665 2282 181 4157 1914 2440 3840 4032 2319 58 3280 4063 3982 3308 3730 4407 665 1637 3872 487 3359 2452 3758 3160 4487 1292 3594 3007 2322 4395 1402 987 3029 2934 1495 4942 374 334 3974 2692 391 3605 3106 725 3264 1835 131 3928 3471 354 4415 3181 2805 4524 1340 2291 2168 4933 1650 4489 680 4403 1827 3708 2336 3321 1 2709 3654 326 1752 397 3930 4857 2473 2194 1691 2603 2473 161 4309 1887 3341 2113 1411 1033 756 4930 965 2405 4418 2996 3159 1245 3055 494 4565 4408 4555 4571 4733 1306 1319 15 1163 3791 3560 2853 2745 1032 4366 2053 4271 4058 518 2033 90 1273 1962 2407 29 1379 402 3187 2623 4809 32 3540 4216 4586 3110 3948 892 780 314 3406 4570 3873 1258 3666 1257 1975 2071 1879 1033 2588 3911 1122 3860 2224 4880 240 3602 282 3426 2577 90 4809 2468 657 4395 577 4604 1638 2708 1270 1395 3629 1494 4004 2294 2750 979 4364 980 2011 1951 4890 3132 2162 2113 4364 2401 2067 4645 2178 995 1086 1987 3462 1742 2733 390 2697 722 3097 318 2116 1725 1812 1119 370 913 2097 4734 1893 459 3036 3134 4943 1550 1599 4306 302 3665 302 2480 4659 2739 818 3120 4480 4902 4861 3528 1975 2957 198 442 4681 2009 1560 50 2921 9 1135 1165 1819 523 4299 1761 2072 2249 1066 2373 913 1367 1204 1923 4105 3373 1394 4936 3274 1254 4816 1600 4210 13 2041 242 3373 4953 1643 2645 4961 4130 3810 1779 4652 4460 4892 1723 1708 957 447 3972 3676 1651 2246 4132 23 3639 420 4649 1244 1587 1248 1805 1599 4641 3398 4971 4593 1392 2615 905 521 2776 2683 1524 3587 3926 3246 294 4883 3693 617 4910 1695 2862 393 3069 1500 812 2717 4095 2398 317 899 348 4957 4296 1670 901 688 4285 1805 1208 3412 839 4084 1999 4765 2329 3644 4647 2373 4261 908 419 2122 1300 3488 4974 2112 1204 4068 861 2872 1319 1209 4180 614 2878 80 1301 3514 1884 3861 3278 2723 2944 276 2487 1624 3919 3485 349 4531 4392 767 3005 2043 4254 2978 506 1810 3397 1367 4681 4715 3927 213 1681 1804 292 4333 1670 2176 4545 4947 4898 2488 1574 2384 464 492 2220 2164 1375 1611 2930 4379 3653 3536 2356 4159 1697 2104 1877 2729 3171 803 2941 4851 3958 3233 4183 1979 408 3728 1925 1657 2567 4850 392 3030 1694 2611 1545 3068 4221 4475 2446 4225 4362 1153 4735 2410 3256 2963 138 1426 117 3079 2628 4075 2663 1811 2405 4422 538 682 1078 4456 531 1469 2486 2224 431 4030 291 4651 4856 4088 227 569 240 1314 2978 4848 4276 3116 2625 4393 2546 253 4819 208 3415 2223 4629 304 2904 2058 4759 4787 4878 3596 2010 308 2626 3653 1310 3833 2740 2888 754 4332 4201 3731 531 3477 3198 4507 4221 2095 1111 4039 2302 4525 2613 3282 4828 517 1691 4587 1655 1568 3182 3664 3227 2159 2316 4536 2344 1408 2424 3097 2091 1624 3179 2621 1452 1377 3479 2024 4823 4590 1062 3477 4114 3675 1758 294 543 4801 4880 2197 2720 4413 2212 947 2924 880 482 267 3639 4257 4715 729 2233 4245 4701 36 1973 3179 2060 1796 2768 4473 272 3234 4499 3381 3527 1393 3181 4758 4941 901 522 2153 3199 3445 4384 32 63 3022 4289 1129 102 2873 374 4802 2908 2346 4332 1319 4141 3452 792 764 1685 290 4145 1563 1683 2325 2672 1623 4577 3193 127 2775 2990 4510 4159 3052 3883 3447 533 3984 2671 906 137 578 4603 4469 1897 3744 2920 4040 4507 956 4329 3 3870 2363 3680 1541 338 3256 4733 464 2383 2722 1326 1541 2126 208 1339 2658 4192 4009 4915 680 938 4517 148 4186 4612 4419 3225 471 1726 3906 473 595 2620 4152 2135 2957 3760 3220 4773 1142 2293 2450 4034 4418 2657 372 3427 3200 732 3341 3880 1669 2858 379 855 3821 4798 431 4291 2875 4336 1116 3470 1956 267 1956 1264 378 175 1036 1519 2468 3485 1904 3237 2494 3627 1664 693 4358 1356 924 1027 4213 1303 3233 4386 2452 3663 3676 326 2999 4791 147 1306 1410 2103 2569 1787 3629 3605 4658 2448 3441 1561 2037 934 188 3700 2979 897 1407 3902 1923 620 1556 1507 1357 359 170 32 2037 4520 1175 2183 825 3936 637 4745 2074 618 4701 1731 4417 3142 4644 1453 427 1183 1504 3405 2079 2911 3659 354 4882 1566 1860 2590 1925 3381 3973 313 2900 147 3847 76 434 836 4821 2508 1453 4521 590 2221 4014 1585 26 4441 4119 2881 4197 1198 2143 2855 2903 3376 4421 4762 965 2697 4495 4938 4361 2394 1436"
# machines = list(map(int, input.rstrip().split()))
# print(minTime(machines, 844676607))
# # print(minTime([2,3], 5))


def maximumSum(a, m):
    # Write your code here
    mod_dict = {}
    max_mod = 0

    for i in range(len(a)):
        a[i] = a[i] % m
        if a[i] > max_mod:
            max_mod = a[i]
        mod_dict[(i, i + 1)] = a[i]

    for l in range(2, len(a) + 1):
        for start in range(0, len(a) - l):
            end = start + l
            mmod = (mod_dict[(start, end - 1)] + a[end - 1]) % m
            if max_mod < mmod:
                max_mod = mmod
            if max_mod == m - 1:
                return max_mod
            mod_dict[(start, end)] = mmod

    return max_mod


# input = "1034055290 1018932065 714950017 381092567 326101711 942764176 1154797858 1394982621 359190020 1326955812 1628062348 1581347180 1000693539 12385708 687152388 2085241463 919008276 252548750 140232206 500819127 32910605 2117032591 485921436 119788917 1931855052 2060517827 679937721 659822237 1613980038 2041919257 78828889 500551679 913367674 793778905 881644245 1239469384 1736543080 2036442102 486968356 2095733099 1215914265 2115030704 1529596631 69124156 2127416411 69265370 6881970 898941038 321814119 147114175"
# arr = list(map(int, input.rstrip().split()))
# m = 1566490300
# print(maximumSum(arr, m))


def max_mult(m, w, x):
    if m < w:
        if x <= w - m:
            m = m + x
            return m * w, m, w
        else:
            m = w
            x = x - (w - m)
            half = x // 2
            m += half
            w += x - half
            return m * w, m, w
    else:
        if x <= m - w:
            w = w + x
            return m * w, m, w
        else:
            w = m
            x = x - (m - w)
            half = x // 2
            m += half
            w += x - half
            return m * w, m, w


def minimumPasses(m, w, p, n):
    # Write your code here
    passes = 1
    c = m * w
    N = c
    while c < n:
        if c + N >= n:
            return passes + 1
        x = c // p
        c = c - x * p
        N, m, w = max_mult(m, w, x)
        c = c + N
        passes += 1
        if passes == 3500:
            print(m, w, c)

    return passes

# print(minimumPasses(5361, 3918, 8447708, 989936375520))

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)

    def add_element(self, data):
        node = self.root
        while True:
            if node.data > data:
                if node.left:
                    node = node.left
                    continue
                else:
                    node.left = Node(data)
            else:
                if node.right:
                    node = node.right
                    continue
                else:
                    node.right = Node(data)



def checkBST_utils(node, mini, maxi):
    bl, br, ul, ur = True, True, [], []
    if not node:
        return True, []
    if node.right:
        if node.right.data > mini and node.right.data < maxi:
            miniv = node.data
            maxiv = maxi
            br, ur = checkBST_utils(node.right, miniv, maxiv)
        else:
            return False, []
    if node.left:
        if node.left.data < maxi and node.left.data > mini:
            miniv = mini
            maxiv = node.data
            bl, ul = checkBST_utils(node.left, miniv, maxiv)
        else:
            return False, []

    lst = ul + ur
    lst.append(node.data)
    return bl and br, lst



def checkBST(root):
    mini = -1*math.inf
    maxi = math.inf
    b, unique = checkBST_utils(root, mini, maxi)
    if b and len(set(unique)) == len(unique):
        return True
    return False


# arr = [1, 2, 4, 3, 5, 6, 7]
#
# tree = Node(3)
#
# tree.left = Node(2)
# tree.right = Node(6)
#
# tree.left.left = Node(1)
# tree.left.right = Node(4)
#
# tree.right.left = Node(5)
# tree.right.right = Node(7)
#
# print(checkBST(tree))


def dfs(adj):
    visited = []

    for i in adj:
        if i[0] not in visited:
            visited

adj = [(1,2), (2,3), (3,4), (4, 1), (5,6)]

class Graph:
    def __init__(self):
        self.g = {}

    def addEdge(self, u, v):
        if u in self.g:
            self.g[u].add(v)
        else:
            self.g[u] = {v}
        if v in self.g:
            self.g[v].add(u)
        else:
            self.g[v] = {u}


def isBalanced(s):
    # Write your code here
    stack = []

    for i in s:

        if i == '(':
            stack.append(')')
        elif i == '{':
            stack.append('}')
        elif i == '[':
            stack.append(']')

        elif i == ')' or i == '}' or i == ']':
            if len(stack) > 0 and stack[-1] == i :
                stack.pop()
            else:
                return "NO"

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"

# s = ["[]][{]{(({{)[})(}[[))}{}){[{]}{})()[{}]{{]]]){{}){({(}](({[{[{)]{)}}}({[)}}([{{]]({{","[]()([{}])[]{}[]",")}{){(]{)([)}{)]())[(})[]]))({[[[)}[((]](])][({[]())","{}()[[((()(({{[]}{}{{[]}}{}}))))]]{{{{([{{{{}}}}])}}}}","{{[()()]}()}(())()()[[[]]][{[]()}(())]"]
#
# for i in s:
#     print(isBalanced(i))


def largestRectangle(h):
    stack = []
    max_area = 0
    h += [0,]
    for i, n in enumerate(h):
        if not stack or n >= stack[-1][1]:
            stack.append((i, n))
        else:
            while stack and stack[-1][1] >= n:
                p = stack.pop()
                max_area = max((i - p[0])*p[1], max_area)
            stack.append((p[0], n))
    return max_area

# h = [1,8,9,1]
# print(largestRectangle(h))

def riddle(arr):
    n = len(arr)
    max_mins = [None]*n
    stack = [] # will store (num, index)
    for i in range(n):
        #print('stack', stack)
        #print('max_mins', max_mins)
        # remember to "push back"
        _m = i
        while len(stack) > 0 and stack[-1][0] > arr[i]:
            _v, _i = stack.pop(-1)
            w = i - _i
            for _w in range(w): # note that it's zero indexed and shifted down
                if max_mins[_w] is None:
                    max_mins[_w] = _v
                else:
                    max_mins[_w] = max(max_mins[_w], _v)
            _m = _i # get the smallest index at which we could start
        stack.append((arr[i],_m))

    # these were the minima for all this time
    while len(stack) > 0:
        #print('stack', stack)
        #print('max_mins', max_mins)
        _v, _i = stack.pop(-1)
        w = n - _i
        for _w in range(w):
            if max_mins[_w] is None:
                max_mins[_w] = _v
            else:
                max_mins[_w] = max(max_mins[_w], _v)
    return max_mins

# h = [2,6,1,12]
# print(riddle(h))

def abbreviation(a, b):
    # Write your code here
    dp = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
    dp[0] = [1 for _ in range(len(a)+1)]
    for k in range(len(b)+1):
        dp[k][0] = 1
    for i in range(1, len(b)+1):
        for j in range(1, len(a)+1):
            if i < len(b)+1 and a[j-1].upper() == b[i-1]:
                dp[i][j] = (dp[i-1][j-1] or dp[i][j-1]) and 1
            elif i < len(b)+1 and a[j-1].isupper() and a[j-1] is not b[i-1]:
                dp[i][j] = (dp[i-1][j-1] or dp[i][j-1]) and 0
            elif i == len(b) and a[j-1].islower():
                dp[i][j] = dp[i][j-1] and 1
            elif i == len(b) and a[j - 1].isupper():
                return "NO"
            else:
                dp[i][j] = (dp[i - 1][j - 1] or dp[i][j - 1]) and 1

    if dp[-1][-1]:
        return "YES"
    else:
        return "NO"




# a = 'MBQEVZPBjcbswirgrmkkfvfvcpiukuxlnxkkenqp'
# b = 'MBQEVZP'
# print(abbreviation(a, b))

# def countDig(n):
#     d = n%10
#     new = n//10
#     if n == 0:
#         return 0
#     return d + countDig(new)

def countDig(n):
    count = 0
    for i in n:
        count += int(i)
    return count

def superDigit(n, k):
    # Write your code here
    # n = int(n)
    count = countDig(n)*k
    while len(str(count)) > 1:
        count = countDig(str(count))
    return count

# n = '7404954009694227446246375747227852213692570890717884174001587537145838723390362624487926131161112710589127423098959327020544003395792482625191721603328307774998124389641069884634086849138515079220750462317357487762780480576640689175346956135668451835480490089962406773267569650663927778867764315211280625033388271518264961090111547480467065229843613873499846390257375933040086863430523668050046930387013897062106309406874425001127890574986610018093859693455518413268914361859000614904461902442822577552997680098389183082654625098817411306985010658756762152160904278169491634807464356130877526392725432086439934006728914411061861235300979536190100734360684054557448454640750198466877185875290011114667186730452681943043971812380628117527172389889545776779555664826488520325234792648448625225364535053605515386730925070072896004645416713682004600636574389040662827182696337187610904694029221880801372864040345567230941110986028568372710970460116491983700312243090679537497139499778923997433720159174153'
# print(superDigit(n, 10000))

def orangesRotting(grid):
    q = []
    time = 0

    n = len(grid)
    m = len(grid[0])

    # find the first rotten orange
    i, j = 0, 0
    for k in range(n):
        for l in range(m):
            if grid[k][l] == 2:
                i, j = k, l
                break

    q.append((i, j))

    while q:
        right, left, up, down = 0, 0, 0, 0
        i, j = q.pop(0)
        if i - 1 >= 0:
            # up = grid[i-1][j]
            if grid[i - 1][j] == 1:
                grid[i - 1][j] = 2
                q.append((i - 1, j))
                up = 1
        if i + 1 < n:
            # down
            if grid[i + 1][j] == 1:
                grid[i + 1][j] = 2
                q.append((i + 1, j))
                down = 1
        if j - 1 >= 0:
            # left
            if grid[i][j - 1] == 1:
                grid[i][j - 1] = 2
                q.append((i, j - 1))
                left = 1
        if j + 1 < m:
            # right
            if grid[i][j + 1] == 1:
                grid[i][j + 1] = 2
                q.append((i, j + 1))
                right = 1

        if right or left or up or down:
            time += 1
    return time

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))