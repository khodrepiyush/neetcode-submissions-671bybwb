class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = {0:1}
        n=len(nums)
        total_sum =0
        res=0
        for i in range(n):
            total_sum+=nums[i]
            res+=sum_map.get(total_sum-k,0)
            sum_map[total_sum] = sum_map.get(total_sum,0)+1

        return res
                


        