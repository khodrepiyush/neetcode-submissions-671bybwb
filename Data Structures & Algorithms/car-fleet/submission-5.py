class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_time = [(i,(target-i)/j) for (i,j) in zip(position,speed)]
        pos_time.sort(reverse=True)

        t1=res= 0
        for pos,t2 in pos_time:
            if t2>t1:
                t1 = t2
                res+=1
        return res
            
          
        
            



        