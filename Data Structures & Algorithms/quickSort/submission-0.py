# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        e = len(pairs) - 1
        s = 0
        arr=self.quickSortImp(pairs, s, e)
        return arr
    
    def quickSortImp(self, pairs:List[Pair], s:int, e:int)->List[Pair]:
        if e-s+1<=1:
            return pairs
        
        pivot = pairs[e]
        left = s
        for i in range(s,e):
            if pairs[i].key < pivot.key:
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1

        pairs[e] = pairs[left]
        pairs[left] = pivot

        self.quickSortImp(pairs, s, left-1)
        self.quickSortImp(pairs, left+1, e)

        return pairs
        