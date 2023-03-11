

class Solution:
    def selectionsort(self, arr):
        for k in range (0, len(arr)-1):
            i = k
            for j in range (k+1, len(arr)):
                if arr[j] < arr[i]:
                    i = j
            if i != k:
                temp = arr[i]
                arr[i] = arr[k]
                arr[k] = temp
        return arr


s = Solution()
arr = [2, 5, 3, 4, 1]
output = s.selectionsort(arr)
assert [1, 2, 3, 4, 5] == output


arr = [10, 7, 5, 3, 10, 2, 14]
output = s.selectionsort(arr)
assert[2, 3, 5, 7, 10, 10, 14] == output