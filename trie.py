words = ["sayali"]

trie = {}

for word in words:
    node = trie
    for w in word:
        # node = node.setdefault(w, {})
        node[w] = {}
        node = node[w]

# print(trie)

words = ["sayali", "sayalu"]

trie1 = {}

for word in words:
    node = trie1
    for w in word:
        node = node.setdefault(w, {})

print(trie1)
#
#
# print(hash(str(trie)))
# print(hash(str({'s': {'a': {'y': {'a': {'l': {'i': {}}}}}}})))

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.child = None
#
#
# n = Node(1)
# n1 = Node(1)
#
# print(hash(n))
# print(hash(n1))


# def maxSubArray(nums):
#     # Initialize our variables using the first element.
#     current_subarray = max_subarray = nums[0]
#
#     # Start with the 2nd element since we already used the first one.
#     for num in nums[1:]:
#         # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
#         current_subarray = max(num, current_subarray + num)
#         max_subarray = max(max_subarray, current_subarray)
#
#     return max_subarray
#
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSubArray(nums))