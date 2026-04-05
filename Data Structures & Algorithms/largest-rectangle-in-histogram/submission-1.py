class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea=0
        n=len(heights)
        stack=[]
        for idx,h in enumerate(heights):
            i=idx
            while stack and h<stack[-1][1]:
                i,hgt=stack.pop()
                maxarea=max(maxarea,(idx-i)*hgt)
            idx=i
            stack.append((idx,h))
        while stack:
            i,hgt=stack.pop()
            maxarea=max(maxarea,(n-i)*hgt)
        return maxarea


        