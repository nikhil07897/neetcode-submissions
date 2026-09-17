class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in hash:
                l = max([s[r]] + 1, 1)
            hash[s[r]] = r
            res = max(res,r - 1 + 1)
        return res

        