class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        heapq.heapify_max(maxHeap)

        while len(maxHeap) > 1:
            result = heapq.heappop_max(maxHeap) - heapq.heappop_max(maxHeap)
            heapq.heappush_max(maxHeap, result)
            
        return 0 if not maxHeap else maxHeap[0]
        