class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        arr_sum=0
        l=0
        res=n+1
        for r in range(n):
            arr_sum+=nums[r]
            while l<r and arr_sum>target:
                res = min(res,r-l+1)
                arr_sum-=nums[l]
                l+=1
            if arr_sum >= target:
                res = min(res,r-l+1)

        return 0 if res==n+1 else res
                






        