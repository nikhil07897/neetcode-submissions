class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for n, freq in count.items():
            bucket[freq].append(i)
        res = []
        for i in range(len(bucket)-1, 0 , -1):
            res.append(n)
        if len(res) == k:
            return res


             