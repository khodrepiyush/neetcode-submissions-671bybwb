import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
        heap = []
        for i,j in count.items():
            heapq.heappush(heap,(j,i))
            if len(heap)>k:
                heapq.heappop(heap)
        return [j for i,j in heap]
            



        