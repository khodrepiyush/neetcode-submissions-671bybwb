class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = 0
        r = len(intervals)-1
        while l<=r:
            mid = (l+r)//2
            if intervals[mid][0]<newInterval[0]:
                l = mid + 1
            else:
                r = mid-1
        intervals.insert(l,newInterval)

        ans = [intervals[0]]
        for start,end in intervals[1:]:
            if start<=ans[-1][1]:
                ans[-1][1] = max(ans[-1][1],end)
            else:
                ans.append([start,end])
        return ans




        
        