class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(n,i):
            left = 2*i +1
            right = 2*i +2

            largest = i
            if left<n and nums[left]>nums[largest]:
                largest = left
            if right<n and nums[right]>nums[largest]:
                largest = right
            if largest!=i:
                nums[i],nums[largest] = nums[largest],nums[i]
                heapify(n,largest)

        n = len(nums)
        for i in range(n//2-1,-1,-1):
            heapify(n,i)
        
        for i in range(n-1):
            nums[n-1-i],nums[0] = nums[0],nums[n-1-i]
            heapify(n-1-i,0)
        return nums

            

                


