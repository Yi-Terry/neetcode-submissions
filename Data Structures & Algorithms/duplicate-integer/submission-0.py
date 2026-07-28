class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_check = set(nums)
        if len(nums) == len(dup_check):
            return False 
        else:
            return True
