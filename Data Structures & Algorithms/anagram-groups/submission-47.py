class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        
        for s in strs:

            count = [0] * 26

            for c in s:

                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())

        # Time: O(m * n), m being the length of the list and n being the length of the string
        # Space: O(m)