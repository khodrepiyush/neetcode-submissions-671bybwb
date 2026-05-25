class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        winner = 0
        votes = 0
        for i in nums:
            if votes == 0:
                winner = i
                votes = 1
            elif i == winner:
                votes+=1
            else:
                votes-=1
        return winner

        