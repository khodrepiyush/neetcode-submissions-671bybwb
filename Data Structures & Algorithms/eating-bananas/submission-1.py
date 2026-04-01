class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        def hrs(arr,spd):
            res=0
            for i in arr:
                res+=(i+spd-1)//spd
            return res

        #binary search
        res=0
        l=1
        r=max(piles)
        while l<=r:
            mid=(l+r)//2
            if hrs(piles,mid)<=h:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res



        
        