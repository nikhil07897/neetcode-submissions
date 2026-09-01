class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = 1 + need.get(c, 0)
        count = l = 0
        res = ""
        for r in range(len(s)):
            if s[r] in need:
                need[s[r]] -= 1
                if need[s[r]] >= 0:
                    count += 1
            while count == len(t):
                if not res or r - l + 1 < len(res):
                    res = s[l: r + 1]
                if s[l] in need:
                    need[s[l]] += 1
                    if need[s[l]] > 0:
                        count -= 1
                l += 1
        return res                   