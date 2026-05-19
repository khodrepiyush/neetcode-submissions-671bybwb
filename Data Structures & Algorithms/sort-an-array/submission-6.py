import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums,l,r):
            ran = random.randint(l,r)
            nums[ran],nums[r] = nums[r],nums[ran]
            ptr =l
            pivot=nums[r]
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[i],nums[ptr]=nums[ptr],nums[i]
                    ptr+=1
            nums[ptr],nums[r] = nums[r],nums[ptr]
            return ptr
        
        def quicksort(nums,l,r):
            if l<r:
                ptr=partition(nums,l,r)
                quicksort(nums,l,ptr-1)
                quicksort(nums,ptr+1,r)
        quicksort(nums,0,len(nums)-1)
        return nums





                



        
        