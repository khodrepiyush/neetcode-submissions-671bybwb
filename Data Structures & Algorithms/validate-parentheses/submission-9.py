class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {'(':')', '{':'}', '[':']'}
        stack = []
        for char in s:
            if char in (')','}',']'):
                if stack and bracket_map[stack[-1]]==char:
                        stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
                    
            
        