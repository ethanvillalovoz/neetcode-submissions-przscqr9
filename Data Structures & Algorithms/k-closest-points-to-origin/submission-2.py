class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for x, y in points:
            dist = ((x-0)**2 + (y-0)**2)**(1/2)
            heapq.heappush(heap, (dist, x, y))

        res = []

        while k > 0:
            dist, x, y = heapq.heappop(heap)
            res.append([x,y])
            k -= 1

        return res