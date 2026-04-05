class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i,val in enumerate(temperatures):
            while stack and stack[-1][1]<val:
                idx,v=stack.pop()
                res[idx]=i-idx
            stack.append((i,val))
        return res
        
        