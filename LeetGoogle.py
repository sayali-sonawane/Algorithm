class LongSubString:
    def __init__(self):
        pass

    def longestSubNoRepeat(self, s):
        # Use unicode
        # characters = [0 for _ in range(256)]

        # use dictionary
        characters = {}

        length = 0
        for c in s:
            # if characters[ord(c)] == 0:
            # length += 1
            # characters[ord(c)] = 1
            if c not in characters:
                length += 1
                characters[c] = 1
        return length


# l = LongSubString()
# print(l.longestSubNoRepeat("pwwkew"))

class WaterTank:
    def __init__(self):
        pass

    def maxWater(self, arr):
        n = len(arr)
        i, j = 0, n - 1

        maxArea = 0

        while abs(i - j) > 1:
            area = (j - i) * min(arr[i], arr[j])
            if area > maxArea:
                maxArea = area

            if arr[i] < arr[j]:
                i = i + 1
            else:
                j = j - 1

        return maxArea

# w = WaterTank()
# height = [1,2,1]
# print(w.maxWater(height))

def twoSum(nums, target):
    d = dict()
    for i, val in enumerate(nums):
        d[val] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        ind = d.get(complement)
        if ind and ind != i:
            return [i, ind]

# n = [2,7,11,15]
# print(twoSum(n, 9   ))

def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if n == 1:
        return nums
    i = n - 1

    flag = True
    inverted = False
    seen = []

    while flag:
        if i == 0 and nums[i] > nums[i + 1]:
            seen.append(nums[i])
            flag = False
            inverted = True
        if nums[i] < nums[i - 1]:
            seen.append(nums[i])
            i -= 1
        else:
            seen.append(nums[i])
            i -= 1
            flag = False

    if inverted:
        return sorted(nums)

    nums = nums[:i+1]

    seen = sorted(seen)
    j = 0
    while nums[i] > seen[j]:
        j += 1

    left = nums[i]
    right = seen[j]

    nums[i] = right
    seen.append(left)
    seen.remove(right)


    nums = nums + sorted(seen)
    return nums

# print(nextPermutation([1]))

# def canJump(nums):
#     n = len(nums)
#     mat = [[False for _ in range(n)] for _ in range(n)]
#
#     mat[0][0] = True
#
#     for i in range(n):
#         start = i
#         if i == 0:
#             start = 1
#         for j in range(start, n):
#
#             prev_col = []
#
#             for l in range(n):
#                 col = i - 1
#                 if i == 0:
#                     col = 0
#                 prev_col.append(mat[l][col])
#
#             if sum(prev_col) > 0:
#                 # for k in range(1, nums[i] + 1):
#                 if j + k < n:
#                     mat[i][j + k] = True
#     for i in range(n):
#         if mat[i][n - 1] == True:
#             return True
#     return False

# nums = [3,2,1,0,4]
# print(canJump(nums))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):

    node1 = l1
    node2 = l2
    out = ListNode()
    node3 = out

    carry = 0

    while node1 is not None or node2 is not None:
        val1, val2 = 0, 0
        sums = 0

        if node1:
            val1 = node1.val
        if node2:
            val2 = node2.val
        sums = val1 + val2 + carry
        node3.val = sums % 10

        carry = sums // 10

        if carry or node1.next or node2.next:
            node3.next = ListNode()

        if node1: node1 = node1.next
        if node2: node2 = node2.next
        node3 = node3.next
    return out

s = [1,2,4]
t = [1,3,4]
#
s_n = ListNode()
s_node = s_n
for j,i in enumerate(s):
    s_node.val = i
    if j < len(s)-1:
        s_node.next = ListNode()
        s_node = s_node.next
#
t_n = ListNode()
t_node = t_n
for j,i in enumerate(t):
    t_node.val = i
    if j < len(s)-1:
        t_node.next = ListNode()
        t_node = t_node.next
# addTwoNumbers(s_n, t_n)

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    first = head
    second = head
    for _ in range(n):
        if second:
            second = second.next
        else:
            return None

    while second and second.next:
        second = second.next
        first = first.next

    if second:
        first.next = first.next.next
    else:
        return None

    return head

# removeNthFromEnd(s_n, 1)

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None and l2 == None:
        return None
    if l1 == None:
        return l2
    if l2 == None:
        return l1

    node1 = l1
    node2 = l2

    out = ListNode()
    node3 = out

    # merging while both are existing
    while node1 and node2:

        if node1.val < node2.val:
            node3.val = node1.val
            node1 = node1.next
        else:
            node3.val = node2.val
            node2 = node2.next

        if node1 and node2:
            node3.next = ListNode()

        if node3.next: node3 = node3.next

    if node1:
        node3.next = node1

    if node2:
        node3.next = node2

    return out

# mergeTwoLists(s_n, t_n)

def lengthOfLongestSubstringTwoDistinct(s):
    n = len(s)

    from collections import Counter
    count = Counter()

    left, right = 0, 0
    max_len = -1

    unique = 0

    while right < n:
        cr = s[right]

        count[cr] += 1

        if len(count) > 2:
            while left <= right and len(count) > 2:
                cl = s[left]
                count[cl] -= 1
                if count[cl] == 0:
                    del count[cl]
                left += 1
        if len(count) <= 2:
            max_len = max(max_len, sum(count.values()))
        right += 1
    return max_len

# s = "eceba"
# print(lengthOfLongestSubstringTwoDistinct(s))

def findMissingRanges(nums, lower, upper):
    out = []

    nums = [lower] + nums + [upper]

    for i, v in enumerate(nums):
        if nums[i] == nums[i + 1] or nums[i] + 1 == nums[i + 1]:
            continue
        first = nums[i] + 1
        last = nums[i + 1] - 1
        if last == first:
            ans = str(last)
        else:
            ans = str(first) + "->" + str(last)
        out.append(ans)

    return out

# a = [0,1,3,50,75]
# l = 0
# u = 99
# print(findMissingRanges(a, l, u))

def nextClosestTime(time):
    # from copy import deepcopy
    # time = [int(time[0]), int(time[1]), int(time[3]), int(time[4])]
    # max_vals = [2, 9, 5, 9]
    # out = deepcopy(time)
    # sort = list(sorted(set(time)))
    # n = 4
    #
    # def isValid(time):
    #     num = time[2] * 10 + time[3]
    #     minutes = False
    #     if 0 <= num <= 59:
    #         minutes = True
    #     hours = False
    #     num = time[0] * 10 + time[1]
    #     if 0 <= num <= 23:
    #         hours = True
    #     return hours and minutes
    #
    # def greater(out, time):
    #     out = out[0] * 1000 + out[1] * 100 + out[2] * 10 + out[3]
    #     time = time[0] * 1000 + time[1] * 100 + time[2] * 10 + time[3]
    #     if out > time:
    #         return True
    #     return False
    #
    # for i in range(n - 1, -1, -1):
    #     valid = False
    #     curr = time[i]
    #     while valid == False:
    #         if curr == sort[-1] or curr == max_vals[i]:
    #             out[i] = sort[0]
    #         else:
    #             curr = sort[sort.index(curr) + 1]
    #             out[i] = curr
    #         valid = isValid(out)
    #     larger = greater(out, time)
    #     if valid and larger:
    #         break
    # out = str(out[0]) + str(out[1]) + ":" + str(out[2]) + str(out[3])
    # return out
    from copy import deepcopy

    time = list(time)
    digits = deepcopy(time)
    digits.remove(':')
    digits = sorted(set(digits))

    for i, lim in ((4, '9'), (3, '5'), (1, '9'), (0, '2')):
        if i == 1 and time[0] == '2':
            lim = '3'

        flag = True
        for d in digits:
            if time[i] < d <= lim:
                time[i] = d
                flag = False
                break
        if flag == False:
            break
        if flag:
            time[i] = digits[0]


    return ''.join(time)

# t = "19:34"
# print(nextClosestTime(t))

def expressiveWords(s, words):
    import collections
    count = 0
    s = collections.Counter(s)
    s = collections.OrderedDict(sorted(s.items()))
    for w in words:
        flag = True
        w = collections.Counter(w)
        w = collections.OrderedDict(sorted(w.items()))
        for k1, v1 in w.items():
            if k1 in s and (v1 == s[k1] or s[k1] // v1 == 3 or float(s[k1]) / v1 == 2.5):
                continue
            else:
                flag = False
        if flag:
            count += 1
    return count

# s = "heeellooo"
# w = ["hello", "hi", "helo"]
# s = "zzzzzyyyyy"
# w = ["zzyy","zy","zyy"]
# print("expressive words", expressiveWords(s, w))

def trap(height):
    i = 0
    n = len(height)
    area = 0
    asc_i, des_i = 0, 0
    while i < n:
        i += 1
        asc = False
        des = False

        if i < n and height[i] < height[i - 1]:
            des = True
            while i < n and height[i] < height[i - 1]:
                i += 1
            des_i = i - 1

        if des and i < n and height[i] > height[i - 1]:
            asc = True
            while i < n and height[i] > height[i - 1]:
                i += 1
            asc_i = i - 1

        if asc and des:
            area += (asc_i - des_i - 1) * min(height[asc_i], height[des_i])

    return area

# a = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(trap(a))

def ladderLength(beginWord, endWord, wordList):
    def word_diff(w1, w2):
        diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
        if diff == 1:
            return True
        return False

    from collections import defaultdict

    adj_list = defaultdict(list)

    for w in wordList:
        for wd in wordList:
            if word_diff(w, wd):
                adj_list[w].append(wd)
                adj_list[wd].append(w)
    for w in wordList:
        if word_diff(beginWord, w):
            adj_list[beginWord].append(w)
            adj_list[w].append(beginWord)

    q = [beginWord]
    visited = [beginWord]
    length = 0
    while q:
        node = q.pop(0)
        for n in adj_list[node]:
            if n not in visited:
                if n == endWord:
                    return length + 1
                q.append(n)
                visited.append(n)
                length += 1

    return 0

# a = "hit"
# b = "cog"
# c = ["hot","dot","dog","lot","log","cog"]
# print(ladderLength(a, b, c))
from collections import defaultdict
from copy import deepcopy

def findOrder(numCourses, prerequisites):
    pre_req = defaultdict(list)
    post_req = defaultdict(list)

    out = []

    for l in prerequisites:
        pre_req[l[0]].append(l[1])
        post_req[l[1]].append(l[0])

    # find sync
    syncs = []
    source = prerequisites[0][0]
    source_q = [source]

    while source_q:
        node = source_q.pop(0)
        if post_req[node]:
            for n in post_req[node]:
                if post_req[n]:
                    source_q.append(n)
                else:
                    syncs.append(n)
        else:
            syncs.append(node)

    queue = deepcopy(syncs)
    while queue:
        curr = queue.pop(0)
        if curr not in out:
            out.append(curr)
        for n in pre_req[curr]:
            queue.append(n)

    return out[::-1]

# a = [[1,0],[2,0],[3,1],[3,2]]
# n = 4
# print(findOrder(n, a))

def braceExpansionII(expression):
    from functools import reduce
    n = len(expression)

    def helper(e, index):
        s = [[]]
        while index < n:
            if e[index] == "{":
                t, i = helper(e, index + 1)
                s[-1].append(t)
                index = i
            elif e[index] == "}":
                index += 1
                break
            elif e[index] == ",":
                s.append([])
                index += 1
            else:
                s[-1].append(e[index])
                index += 1
        res = set()
        for a in s:
            # multiply
            x = reduce(lambda x, y: {i + j for i in x for j in y}, a)
            # append
            res.update(x)
        return list(res), index

    s, _ = helper(expression, 0)
    s.sort()
    return s

# e = "{{a,z},a{b,d{c,e}}{c,d}{e,f},{ab,z}}"
# print(braceExpansionII(e))

def braceExpansionI(expression):
    # e = '2[3[a]b]abc'
    n = len(expression)

    def helper(e, idx):
        # returns string and index
        s = []
        while idx < n:
            if e[idx] == '[':
                loops = 1
                if 48 <= ord(e[idx-1]) <= 57:
                    loops += (int(e[idx-1]) - 1)
                idx += 1
                t, idx = helper(e, idx)
                t = t*(loops)
                s.append(t)
            elif e[idx] == ']':
                idx += 1
                break
            elif 48 <= ord(e[idx]) <= 57:
                # s[-1][-1][-1] = int(e[idx])
                idx += 1
                continue
            else:
                s.append(e[idx])
                idx += 1

        s = ''.join(s)

        return s, idx

    res, _ = helper(expression, 0)

    return res




# e = '1[[a]b]abc'
# print(braceExpansionI(e))