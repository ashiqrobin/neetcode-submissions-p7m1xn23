class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, val in enumerate(nums):
            search_val = target - val
            if search_val in dic:
                return [dic[search_val], index]
            else:
                dic[val] = index
        