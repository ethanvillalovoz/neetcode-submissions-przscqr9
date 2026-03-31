class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap)
            x = heapq.heappop(maxHeap)

            if x == y:
                continue
            else:
                heapq.heappush(maxHeap, (y-x))

        if maxHeap:
            return -maxHeap[0]
        else:
            return 0