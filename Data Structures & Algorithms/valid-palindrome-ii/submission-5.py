class Solution:
    def __init__(self):
        self.one_char_used = False
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if self.one_char_used == True:
                    return False
                else:
                    self.one_char_used = True
                    if self.validPalindrome(s[l:r]) or self.validPalindrome(s[l+1:r+1]):
                        return True
                    else:
                        return False
            l += 1
            r -= 1
        return True
                
            

            
            

        