class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}

        for i in s:
            count1[i]= count1.get(i,0)+1
        
        for j in t:
            if j not in count1:
                return False
            else:
                count1[j]-=1
        for i in count1.values():
            if i!=0:
                return False
        return True
        

        
        