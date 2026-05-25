class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # create hashmap 
        for n in nums:
            count[n] = count.get(n,0) + 1 # freq add count
        bucket = [[] for _ in range(len(nums) + 1)]# create bucket
        for n, freq in count.items():
            bucket[freq].append(n)
        res = []
        for i in range((len(nums)) -1, 0, -1):
            for n in bucket[i]:
                res.append[n]
            if len(res) == k:
                return res

             