class Sorting:
    def __init__(self):
        pass

    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr

        pivot = 0
        n = len(arr)
        i = 0
        j = n-1

        while j > i:
            if arr[j] <= arr[pivot] <= arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

            for k in range(i, n):
                if arr[k] > arr[pivot]:
                    i = k
                    break
            for l in range(j, 0, -1):
                if arr[l] < arr[pivot]:
                    j = l
                    break
        arr[pivot],arr[j] = arr[j],arr[pivot]

        left = self.quickSort(arr[:j])
        curr = [arr[j]]
        right = self.quickSort(arr[j+1:])

        return left + curr + right

    def _merge(self, arr1, arr2):
        n1 = len(arr1)
        n2 = len(arr2)
        out = []

        i,j = 0,0

        while len(out) < n1+n2:
            if i == n1 or j == n2:
                break
            if arr1[i] <= arr2[j]:
                out.append(arr1[i])
                i += 1
            elif arr2[j] < arr1[i]:
                out.append(arr2[j])
                j += 1

        if i < n1:
            out = out + arr1[i:]
        if j < n2:
            out = out + arr2[j:]

        return out

    def mergeSort(self, arr):
        n = len(arr)
        half = n//2
        if n == 1:
            return arr

        left = self.mergeSort(arr[:half])
        right = self.mergeSort(arr[half:])

        return self._merge(left, right)


arr = [10,16,8,12,15,6,3,9,5]
s = Sorting()

print(s.mergeSort(arr))