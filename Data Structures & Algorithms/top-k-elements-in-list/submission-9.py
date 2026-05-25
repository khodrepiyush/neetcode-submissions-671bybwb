class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        n = len(nums)
        for i in nums:
            count[i] = count.get(i,0)+1
        
        freq = [[] for i in range(n+1)]

        for item,cnt in count.items():
            freq[cnt].append(item)
        res = []
        for i in range(n,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res





        
        

        