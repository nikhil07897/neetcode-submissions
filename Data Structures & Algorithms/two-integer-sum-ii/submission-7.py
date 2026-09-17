class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            curSum = numbers[1] + numbers[r]
            
            if CurSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return[l + 1, r + 1]