class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n =len(nums)
        res = [0]*n
        l = 0
        r = n-1
        resindex = n-1
        while l<=r:
            if nums[l]**2>nums[r]**2:
                res[resindex]= nums[l]**2
                l+=1
            else:
                res[resindex]= nums[r]**2
                r-=1
            resindex-=1
        return res



        