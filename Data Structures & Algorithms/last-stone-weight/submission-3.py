class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap)
            x = heapq.heappop(maxHeap)

            if y == x:
                continue
            else:
                heapq.heappush(maxHeap, (y-x))

        return -maxHeap[0] if maxHeap else 0