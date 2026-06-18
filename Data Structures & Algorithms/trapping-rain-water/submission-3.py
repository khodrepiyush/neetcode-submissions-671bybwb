class Solution:
    def trap(self, height: List[int]) -> int:
        res =0
        l =0
        r=len(height)-1
        lmax = height[l]
        rmax=height[r]
        while l<=r:
            if lmax<rmax:
                lmax = max(height[l],lmax)
                res+=(lmax-height[l])
                l+=1
            else:
                rmax = max(height[r],rmax)
                res+=(rmax-height[r])
                r-=1
        return res



        