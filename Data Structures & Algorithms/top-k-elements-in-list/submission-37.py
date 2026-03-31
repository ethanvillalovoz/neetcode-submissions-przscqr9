class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        arr = []

        for num, count in counter.items():
            arr.append([count, num])

        arr.sort(key=lambda x: x[0])

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])

        return res