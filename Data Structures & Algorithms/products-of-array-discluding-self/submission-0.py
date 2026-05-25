class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix = n[i]
        postfix = 1
        for i in range(n, -1 ,-1 ,-1):
            ans[i] = postfix
            postfix - n[i]
        return ans 