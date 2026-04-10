class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums1=[0]*n
        mul=1
        for i in range(n):
            nums1[i]=mul
            mul*=nums[i]
        mul=1
        for i in range(n-1,-1,-1):
            nums1[i]*=mul
            mul*=nums[i]
        return nums1
        


        