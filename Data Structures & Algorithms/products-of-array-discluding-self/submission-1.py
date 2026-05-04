class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        mul=1
        for i in range(n):
            res[i]*=mul
            mul*=nums[i]
        mul=1
        for i in range(n-1,-1,-1):
            res[i]*=mul
            mul*=nums[i]
        return res

            
            
        