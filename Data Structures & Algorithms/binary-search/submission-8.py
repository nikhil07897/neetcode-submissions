class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , m = 0, len(nums) - 1
        while l <= re:
            m = l + ((r - l)// 2)
            if nums[m] > target:
                m = r - 1
            elif nums[m] < target:
                m = l + 1
            else:
                return m
        return -1