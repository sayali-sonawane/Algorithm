# def getFactors(n):
#     if n == 1:
#         return []
#     ans = []
#
#     def util(out, target, idx):
#         if target == 1:
#             # temp = sorted(list(out))
#             ans.append(list(out))
#             return
#
#
#         for i in range(idx, target // 2 + 2):
#
#             if target % i == 0 and target >= idx:
#                 out.append(i)
#                 target = target // i
#
#                 util(out, target, idx)
#
#                 out.pop()
#                 target = target * i
#
#     util([], n, 2)
#     return ans

def getFactors(n: int):
    nums = [num for num in range(2, (n // 2 + 1)) if n % num == 0]
    result = []
    combinations = []

    def backTrack(index, currProduct):

        if currProduct == n:
            if combinations:
                result.append(combinations[:])
            return

        if currProduct > n:
            return

        for i in range(index, len(nums)):
            combinations.append(nums[i])
            backTrack(i, currProduct * nums[i])
            combinations.pop()

    backTrack(0, 1)
    return result

# print(getFactors(32))

def evalRPN(tokens):
    ans = 0

    def util(arr, i):
        nonlocal ans
        if len(arr) == 1:
            ans = arr[0]
            return
        for i in range(len(arr)):
            if arr[i] in ("+", "-", "*", "/"):
                first = int(arr[i - 2])
                second = int(arr[i - 1])
                temp = 0
                if arr[i] == '+':
                    temp = first + second
                elif arr[i] == '-':
                    temp = first - second
                elif arr[i] == '*':
                    temp = first * second
                elif arr[i] == '/':
                    temp = int(first / second)
                arr[i] = temp
                arr.pop(i-2)
                arr.pop(i-2)
                if len(arr) >= 1:
                    return util(arr, i)

    util(tokens, 0)
    return ans

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))