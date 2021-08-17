# Input
# "hotelfate"
# is_word() -> bool
#
# Output
# all valid partitionings of string
# [["hotel", "fate"],
# ["hot", "elf", "ate"]]

# https://stackoverflow.com/questions/8870261/how-to-split-text-without-spaces-into-list-of-words

# fuck it's dynamic programming


def is_word(word):
    if word in ["hotel", "fate", "hot", "elf", "ate"]:
        return True
    return False

# ans = []


def backtrace(place, i, j):
    # if we hit the 0th row, it means we are at the end of recursion
    if i == 0:
        return [[]]

    ans = []
    n = len(place)

    # getting the children
    children = []
    for row in range(n-1, -1, -1):
        if place[row][j] == 1:
            children.append((row, j))

    # recurse through every child and return the results
    for child in children:
        ans1 = backtrace(place, child[0], child[0]-1)
        for l in ans1:
            ans.append([child] + l)

    return ans


def SplitWord(string):
    n = len(string)
    place = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            curr = string[i:j+1]
            if is_word(curr):
                place[i][j] = 1

    n = len(place)
    return backtrace(place, n-1, n-1)





print(SplitWord("hotelfate"))