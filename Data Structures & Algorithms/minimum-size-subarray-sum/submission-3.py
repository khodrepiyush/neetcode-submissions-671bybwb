class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        arr_sum=0
        l=0
        res=n+1
        for r in range(n):
            arr_sum+=nums[r]
            while arr_sum>=target:
                res = min(res,r-l+1)
                arr_sum-=nums[l]
                l+=1
        return res%(n+1)
                






        