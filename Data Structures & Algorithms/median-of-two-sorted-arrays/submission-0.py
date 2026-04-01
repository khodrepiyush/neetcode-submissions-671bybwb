class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)

        lft_hlf_cnt=(m+n)//2

        if n<m:
            m,n=n,m
            nums1,nums2=nums2,nums1
        
        l=0
        r=m-1
        while True:
            mid=(l+r)//2
            idx=lft_hlf_cnt-mid-2

            left1=nums1[mid] if mid>=0 else -float('inf')
            right1=nums1[mid+1] if mid<m-1 else float('inf')
            left2=nums2[idx] if idx>=0 else -float('inf')
            right2=nums2[idx+1] if idx<n-1 else float('inf')

            if left1<=right2 and left2<=right1:
                if (m+n)%2==0:
                    return (max(left1,left2)+min(right1,right2))/2
                else:
                    return min(right1,right2)
            elif left1>right2:
                r=mid-1
            else:
                l=mid+1



        
        
        