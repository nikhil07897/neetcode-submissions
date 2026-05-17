class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in mpp:
                return [mpp[diff], index]
            mpp[num] = index
        return