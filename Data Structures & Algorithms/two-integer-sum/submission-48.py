class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i , num in enumerate(nums):
            seen = target - num
            if seen in hash:
                return [hash[seen], i]
            hash[num] = i