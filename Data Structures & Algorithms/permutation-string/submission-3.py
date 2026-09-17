class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = {}
        window = {}
        
        for c in s1:
            need[s1[c]] = 1 + need.get(s1[c], 0)
        l = 0
        for r in range(len(s2)):
            window[s2[r]] = 1 + window.get(s2[r], 0)
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                l += 0
            if window == need:
                return True
        return False
        

        

        