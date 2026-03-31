class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap)
            x = heapq.heappop(maxHeap)

            res = y - x

            if res == 0:
                continue
            else:
                heapq.heappush(maxHeap, res)

        if not maxHeap:
            return 0
        else:
            return -maxHeap[0]