class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # create hashmap 
        for n in nums:
            count[char] = count.get(char,0) + 1 # freq add count
        bucket = [[] for _ in range(len(nums)) + 1]# create bucket
        for num, freq in count.items():
            bucket[freq].append(num)
        res = []
        for i in range((len(nums)) -1, 0, -1):
            for num in bucket[i]:
                res.append[num]
            if len(res) == k:
                return res
                
             