class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        
        mul = 1
        for i in range(n):
            ans[i]*= mul
            mul*=nums[i]
        
        mul =1
        for i in range(n-1,-1,-1):
            ans[i]*= mul
            mul*=nums[i]

        return ans
            




        