class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l , r = 0, len(height) - 1
        while l < r:
            area =  (r - l)* min(height[l], height[r])
            res = max(area,res)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

        #res = 0
        #for l in range(len(heights)):
           #for r in range(l+1, len(heights)):
                #area = (r - l ) * min(heights[l], heights[r])
                #res = max(res,area)
        #return res
