class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , m = 0 , len(nums) - 1
        while l <= r:
            m = l + ((r - l)// 2)
            if nums[m] > r:
                r = m - 1
            elif nums[n] > l:
                l = m + 1
            else:
                return m
        return - 1
        