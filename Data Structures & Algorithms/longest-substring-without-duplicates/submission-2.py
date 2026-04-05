class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        dict1={}
        res=0
        for r in range(len(s)):
            if s[r] in dict1:
                if dict1[s[r]]>=l:
                    l=dict1[s[r]]+1
            dict1[s[r]]= r
            res=max(res,r-l+1)
        return res
        
        

            






        