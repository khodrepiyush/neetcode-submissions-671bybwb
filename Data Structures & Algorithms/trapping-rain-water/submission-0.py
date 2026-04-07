class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        max1=[0]*n
        left_max=0
        right_max=0
        ans=0
        for i in range(n):
            left_max=max(left_max,height[i])
            max1[i]=left_max
        
        for i in range(n-1,-1,-1):
            right_max=max(right_max,height[i])
            ans+=min(max1[i],right_max)-height[i]
        return ans

        




        