import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
        heap = [(-j,i) for i,j in count.items()]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            _,j = heapq.heappop(heap)
            res.append(j)
        return res
            



        