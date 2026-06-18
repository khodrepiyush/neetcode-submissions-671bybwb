class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0

        for i in range(n):
            if nums[i] !=0:
                nums[i],nums[l] = nums[l],nums[i]
                l+=1
    
