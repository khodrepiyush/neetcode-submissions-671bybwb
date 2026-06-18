class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if i>0 and nums[i]<=nums[k-1]:
                continue
            nums[k],nums[i] = nums[i],nums[k]
            k+=1
        return k
        

        