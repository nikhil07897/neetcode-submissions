class Solution:
    def isPalindrome(self, s: str) -> bool:
        nstr = ""
        for c in s:
            if c.isalnum():
                nstr += c.lower()
        return nstr == ndtr[::-1]
        