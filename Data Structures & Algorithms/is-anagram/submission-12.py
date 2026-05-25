class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mpp = {}
        for mpp in s:
            mpp[char] = mpp.get(char, 0) + 1
        for mpp in t:
            if char not in mpp:
                return False
            mpp[char] -= 1
            if mpp[char] < 0:
             return False
        return True