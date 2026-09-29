class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for coordiante in points:
            total = 0
            for number in coordiante:
                total += number * number

            heapq.heappush_max(maxHeap, (total, coordiante))

            while len(maxHeap) > k:
                heapq.heappop_max(maxHeap)

        return [res[1] for res in maxHeap]

        