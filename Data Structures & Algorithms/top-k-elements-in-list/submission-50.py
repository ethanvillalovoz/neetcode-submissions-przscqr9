class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        freq = [[] for _ in range(len(nums) + 1)]

        for num, val in count.items():
            freq[val].append(num)

        res = []

        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res

        return res