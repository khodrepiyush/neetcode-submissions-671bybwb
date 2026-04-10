class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for sr in strs:
            res+=str(len(sr))+'#'+sr
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        l,r=0,0
        while r<len(s):
            while s[r]!='#':
                r+=1
            res.append(s[r+1:r+1+int(s[l:r])])
            l,r=r+1+int(s[l:r]),r+1+int(s[l:r])
        print(res)
        return res
            

