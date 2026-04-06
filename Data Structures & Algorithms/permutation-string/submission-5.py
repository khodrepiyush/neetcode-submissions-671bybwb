class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        cnt1={}
        for i in s1:
            cnt1[i]=cnt1.get(i,0)+1
        cnt2={}
        total_cnt=len(cnt1)
        cnt=0
        l=0
        for r,ch in enumerate(s2):
            cnt2[ch]=cnt2.get(ch,0)+1   
            if ch in cnt1:
                if cnt1[ch]==cnt2[ch]:
                    cnt+=1
                elif cnt1[ch]+1==cnt2[ch]:
                    cnt-=1
            if r-l+1>n1:
                if s2[l] in cnt1:
                    if cnt1[s2[l]]==cnt2[s2[l]]:
                        cnt-=1
                    elif cnt1[s2[l]]+1==cnt2[s2[l]]:
                        cnt+=1
                cnt2[s2[l]]-=1
                l+=1
            if cnt==total_cnt:
                return True
        return False
        
    



        