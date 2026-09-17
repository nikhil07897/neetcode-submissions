class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        hash = {}
        l = 0
        res = 0
        for r in range(nums):
            while nums[r] in hash:
                hash.remove(nums[l])
                l += 1
            hash.add(nms[r])
            res = max(res, r - l + 1)
        return res        