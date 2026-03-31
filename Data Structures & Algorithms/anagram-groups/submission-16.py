class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            count = Counter(s)

            count = sorted(count.items(), key=lambda x: x[0])

            res[tuple(count)].append(s)

        return list(res.values())