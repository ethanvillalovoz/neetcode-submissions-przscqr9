class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        min_heap = []

        for num, val in count.items():
            heapq.heappush(min_heap, (val, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []

        for _ in range(k):
            val, num = heapq.heappop(min_heap)
            res.append(num)

        return res