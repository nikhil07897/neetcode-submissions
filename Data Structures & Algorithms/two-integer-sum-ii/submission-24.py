class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(numbers):
            seen = target - num
            if seen in hash:
                return [hash[seen],i +1]
            hash[num[i]] = i +1

            