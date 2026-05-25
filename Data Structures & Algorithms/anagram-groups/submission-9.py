class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in words:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1
            res[tuple(count)].append(words)
        return list(res.values())