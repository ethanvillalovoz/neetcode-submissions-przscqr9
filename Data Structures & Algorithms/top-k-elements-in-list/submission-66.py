class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = collections.defaultdict(int)

        for num in nums:
            count[num] += 1

        heap = []

        for num, val in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, num))
            else:
                heapq.heappushpop(heap, (val, num))

        res = []

        for _ in range(k):
            val, num = heapq.heappop(heap)
            res.append(num)

        return res