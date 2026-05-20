class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        sum1=0
        n=len(people)
        l=0
        r=n-1
        cnt=0
        while l<=r:
            capacity = limit - people[r]
            cnt+=1
            r-=1
            if l<=r and people[l]<=capacity:
                l+=1  
        return cnt



        