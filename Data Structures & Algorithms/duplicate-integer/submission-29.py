class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for num in nums:
            if num not in hash:
                return False
            hash.add(num)
        return True