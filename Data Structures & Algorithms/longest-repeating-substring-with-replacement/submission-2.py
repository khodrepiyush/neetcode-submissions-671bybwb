class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt={}
        res=1
        l=0
        max_freq=1
        for r,ch in enumerate(s):
            cnt[ch]=cnt.get(ch,0)+1
            max_freq=max(max_freq,cnt[ch])
            if r-l+1>max_freq+k:
                cnt[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
            

        