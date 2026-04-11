class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set(nums)
        res=0
        for i in nums:
            cnt=1
            if i-1 not in set1:
                while i+1 in set1:
                    cnt+=1
                    i+=1
                res=max(res,cnt)
        return res
                




        