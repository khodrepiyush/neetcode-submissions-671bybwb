import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
        
        heap = []
        for i in count:
            heapq.heappush(heap,(count[i],i))
            if len(heap)>k:
                heapq.heappop(heap)
        return [i[1] for i in heap]