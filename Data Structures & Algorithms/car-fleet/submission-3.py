class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed=[(i,(target-i)/j) for i,j in zip(position,speed)]
        pos_speed.sort(reverse=True)
        _,t1=pos_speed[0]
        cnt=1
        for _,t2 in pos_speed[1:]:
            if t2>t1:
                cnt+=1
                t1=t2
        return cnt


        
        
        


        