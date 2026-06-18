class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        res = 0
        while l<r:
            if heights[l]<heights[r]:
                res = max(res,heights[l]*(r-l))
                l+=1
            else:
                res = max(res,heights[r]*(r-l))
                r-=1
        return res




        