class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n-1):
            for j in range(1,n-i):
                if nums[j-1] > nums[j]:
                    nums[j-1],nums[j] = nums[j],nums[j-1]
        return nums


        

            


        