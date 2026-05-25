class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        winner = nums[0]
        votes = 1
        for i in nums[1:]:
            if i == winner:
                votes+=1
            else:
                votes-=1
                if votes == 0:
                    winner = i
                    votes = 1
        return winner

        