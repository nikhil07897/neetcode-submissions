class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        count[n] = count.get(n,0) + 1
        bucket = [[]for i in range(len(nums)) + 1]
        for n, freq in count.items():
            bucket[i].append(n)
        res = []
        for i in range(bucket[i]-1,0,-1):
            if n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res 