class Solution:

    def encode(self, strs: List[str]) -> str:
        str1=""
        for i in strs:
            str1+=str(len(i))+'#'+ i
        return str1

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res=[]
        n=len(s)
        l=0
        r=0
        while r<n:
            if s[r]=='#':
                res.append(s[r+1:r+int(s[l:r])+1])
                r+=int(s[l:r])+1
                l=r
            r+=1
        return res




