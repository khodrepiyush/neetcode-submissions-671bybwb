class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt={}
        freq=[[] for i in range(len(nums)+1)]

        for num in nums:
            cnt[num]=cnt.get(num,0)+1
        for num,ct in cnt.items():
            freq[ct].append(num)
        res=[]
        for i in range(len(nums),-1,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res





        
        