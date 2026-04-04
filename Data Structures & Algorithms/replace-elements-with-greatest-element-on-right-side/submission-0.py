class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        tmp = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if arr[j] > tmp:
                    tmp = arr[j]
                else:
                    continue
            arr[i] = tmp
            tmp = 0
        arr[n-1] = -1

        return arr