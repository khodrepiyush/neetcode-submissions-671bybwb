class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_map = {}
        for idx,num in enumerate(nums):
            if num in num_map and idx-num_map[num]<=k:
                return True
            num_map[num] = idx
        return False
        
        