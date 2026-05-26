class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1,candidate2 = None, None
        votes1,votes2 = 0,0

        for i in nums:
            if i == candidate1:
                votes1+=1
            elif i == candidate2:
                votes2+=1
            elif votes1 == 0:
                candidate1 = i
                votes1 = 1
            elif votes2 == 0:
                candidate2 = i
                votes2 = 1
            else:
                votes1-=1
                votes2-=1
        target = len(nums)/3
        res = []
        cnt1 = 0
        cnt2 = 0
        for i in nums:
            if i == candidate1:
                cnt1+=1
            elif i == candidate2:
                cnt2+=1
        if cnt1 > target:
            res.append(candidate1)
        if cnt2 > target:
            res.append(candidate2)
        return res







        


        