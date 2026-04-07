class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt1={}
        for ch in t:
            cnt1[ch]=cnt1.get(ch,0)+1
        
        l=0
        cnt2={}
        need=len(cnt1)
        got=0
        ans_l=0
        ans_r=float('inf')
        for r,ch in enumerate(s):
            cnt2[ch]=cnt2.get(ch,0)+1
            if ch in cnt1 and cnt1[ch]==cnt2[ch]:
                got+=1
            while need==got:
                if r-l+1<ans_r-ans_l+1:
                    ans_r=r
                    ans_l=l
                cnt2[s[l]]-=1
                if s[l] in cnt1 and cnt1[s[l]]-1==cnt2[s[l]]:
                    got-=1
                l+=1


        return s[ans_l:ans_r+1] if ans_r!=float('inf') else ""
            

        