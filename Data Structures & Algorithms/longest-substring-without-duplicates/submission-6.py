class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {} 
        res = 0
        l = 0
        n = len(s)
        for r in range(n):
            if s[r] in char_map and char_map[s[r]]>=l:
                l=char_map[s[r]]+1
            char_map[s[r]]=r
            res=max(res,r-l+1)
        return res
        

            


                
        