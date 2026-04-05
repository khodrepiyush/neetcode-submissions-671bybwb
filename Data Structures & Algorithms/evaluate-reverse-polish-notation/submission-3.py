class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=='+':
                stack.append(stack.pop()+stack.pop())
            elif i=='-':
                stack.append(-(stack.pop()-stack.pop()))
            elif i=='*':
                stack.append(stack.pop()*stack.pop())
            elif i=='/':
                temp=stack.pop()
                stack.append(int(stack.pop()/temp))
            else:
                stack.append(int(i))
        return stack[-1]
