import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums,l,r):
            rand_ind = random.randint(l,r)
            nums[r],nums[rand_ind] = nums[rand_ind],nums[r]
            ptr = l
            for i in range(l,r):
                if nums[i]<=nums[r]:
                    nums[ptr],nums[i] = nums[i],nums[ptr]
                    ptr+=1
            nums[ptr],nums[r] = nums[r], nums[ptr]
            return ptr
        
        def quicksort(nums,l,r):
            if l<r:
                partn = partition(nums,l,r)
                quicksort(nums,l,partn-1)
                quicksort(nums,partn+1,r)
        quicksort(nums,0,len(nums)-1)
        return nums




