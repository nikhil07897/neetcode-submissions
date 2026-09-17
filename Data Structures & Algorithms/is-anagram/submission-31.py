class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for char in s:
            count[ord(s) - ord('a')] += 1
        for char in t:
            count [ord(t) - ord['a']] -= 1
        for val in count:
            if val != 0:
                return False
        return True
