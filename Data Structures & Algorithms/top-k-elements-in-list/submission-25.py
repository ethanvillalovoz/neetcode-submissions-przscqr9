class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        heap = []

        for num, count in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            else:
                heapq.heappushpop(heap, (count, num))

        return [x[1] for x in heap]