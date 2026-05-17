class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            seen = target - n
            if seen in hashmap:
                return [hashmap[seen], i]
            hashmap[n] = i
        