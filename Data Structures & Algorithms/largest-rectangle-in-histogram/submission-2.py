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
        for i,hgt in stack:
            maxarea=max(maxarea,(n-i)*hgt)
        return maxarea


        