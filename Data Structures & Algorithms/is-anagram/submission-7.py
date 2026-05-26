class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count1 = {}
        for i in s:
            count1[i]= count1.get(i,0)+1
        
        for j in t:
            if count1.get(j,0)==0:
                return False
            count1[j]-=1
        return True
        

        
        