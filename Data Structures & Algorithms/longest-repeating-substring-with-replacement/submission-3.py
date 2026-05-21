class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_count = 0
        n=len(s)
        l = 0
        res=0
        for r in range(n):
            count[s[r]]=count.get(s[r],0)+1
            max_count = max(max_count,count[s[r]])
            if r-l+1> max_count+k:
                count[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return res




        