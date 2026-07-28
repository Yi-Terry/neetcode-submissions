class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 #pointers, start of index and last index

        while left <= right: 
            mid = (left + right) // 2 # rounds down for middle
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid +1 # if value of middle is less than the target is on right side of list
                            # this is saying start at one place greater than the original middle for left
            else: # if value of middle is greater than the target is on left side of list
                            # this is saying start at one place less than the original middle for right side
                right = mid - 1 

        return -1