class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = 0
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in CharSet:
                charSet.remove(s[r])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
