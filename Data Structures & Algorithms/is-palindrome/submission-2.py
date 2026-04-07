class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            while not s[l].isalnum() and l<r:
                l+=1
            while not s[r].isalnum() and l<r:
                r-=1
            print(l,r)
            if s[l].lower()==s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True

        