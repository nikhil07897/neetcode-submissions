class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        longest = 0
        for num in nums:
            if (n - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
        