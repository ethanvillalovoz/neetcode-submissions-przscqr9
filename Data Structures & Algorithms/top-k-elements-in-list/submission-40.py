class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        heap = []
        for num, count in counter.items():
            heapq.heappush(heap, (count, num))
            
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]