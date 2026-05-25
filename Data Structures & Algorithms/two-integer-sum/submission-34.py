class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i , n in enumerate(nums):
            seen = target - n
            if seen in hash:
                return [hash[seen], i]
        hash[n] = i